import hashlib
import hmac
import secrets


class CapabilityService:

    @staticmethod
    def generate_code() -> str:
        return secrets.token_urlsafe(24)

    @staticmethod
    def hash_code(code: str) -> str:
        normalized_code = code.strip()

        return hashlib.sha256(
            normalized_code.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def verify_code(code: str, stored_hash: str) -> bool:
        if not code or not stored_hash:
            return False

        provided_hash = CapabilityService.hash_code(code)

        return hmac.compare_digest(
            provided_hash,
            stored_hash
        )
import bcrypt

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
)
from sqlalchemy.exc import IntegrityError

from config import Config
from models import db, User
from services.capability_service import CapabilityService
from services.encryption_service import EncryptionService
from services.validation_service import ValidationService


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

encryption_service = EncryptionService(app.config["AES_KEY"])


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    status = None
    capability_code = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        secret = request.form.get("secret", "").strip()

        if not ValidationService.validate_username(username):
            message = "Username must contain between 3 and 80 characters."
            status = "error"

        elif not ValidationService.validate_email(email):
            message = "Please enter a valid email address."
            status = "error"

        elif not ValidationService.validate_password(password):
            message = (
                "Password must contain at least 8 characters, "
                "including uppercase, lowercase and a digit."
            )
            status = "error"

        elif not secret:
            message = "Sensitive information is required."
            status = "error"

        else:
            existing_user = User.query.filter(
                (User.username == username) | (User.email == email)
            ).first()

            if existing_user:
                message = "A user with this username or email already exists."
                status = "error"

            else:
                password_hash = bcrypt.hashpw(
                    password.encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")

                encrypted_data = encryption_service.encrypt(secret)

                capability_code = CapabilityService.generate_code()
                capability_hash = CapabilityService.hash_code(capability_code)

                new_user = User(
                    username=username,
                    email=email,
                    password_hash=password_hash,
                    encrypted_data=encrypted_data,
                    capability_hash=capability_hash,
                    role="user"
                )

                try:
                    db.session.add(new_user)
                    db.session.commit()

                    message = (
                        "Registration completed successfully. "
                        "Save your capability code securely."
                    )
                    status = "success"

                except IntegrityError:
                    db.session.rollback()
                    message = "This username or email already exists."
                    status = "error"

                except Exception:
                    db.session.rollback()
                    message = "An unexpected error occurred."
                    status = "error"

    return render_template(
        "register.html",
        message=message,
        status=status,
        capability_code=capability_code
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    status = None

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        capability_code = request.form.get(
            "capability_code",
            ""
        ).strip()

        user = User.query.filter_by(email=email).first()

        if not user:
            message = "Invalid login credentials."
            status = "error"

        elif not bcrypt.checkpw(
            password.encode("utf-8"),
            user.password_hash.encode("utf-8")
        ):
            message = "Invalid login credentials."
            status = "error"

        elif not CapabilityService.verify_code(
            capability_code,
            user.capability_hash
        ):
            message = "Invalid capability code."
            status = "error"

        else:
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))

    return render_template(
        "login.html",
        message=message,
        status=status
    )


@app.route("/dashboard")
def dashboard():
    user_id = session.get("user_id")

    if not user_id:
        return redirect(url_for("login"))

    user = db.session.get(User, user_id)

    if not user:
        session.clear()
        return redirect(url_for("login"))

    decrypted_data = encryption_service.decrypt(
        user.encrypted_data
    )

    return render_template(
        "dashboard.html",
        user=user,
        decrypted_data=decrypted_data
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False
    )
