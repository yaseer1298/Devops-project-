from flask import request, jsonify, Blueprint
from flask_mail import Message
from .models import db, Incident
from flask_mail import Mail

routes = Blueprint("routes", __name__)
mail = Mail()

@routes.route("/incidents", methods=["POST"])
def create_incident():
    data = request.json
    incident = Incident(
        title=data["title"],
        description=data["description"]
    )
    db.session.add(incident)
    db.session.commit()

    # email
    # Email sending is temporarily disabled to avoid crashes during development.
# If you want email later, configure MAIL_USERNAME and MAIL_PASSWORD in config.py
# and uncomment the lines below.

# try:
#     msg = Message("New Incident Created",
#                   recipients=["your-email@gmail.com"])
#     msg.body = f"Incident Created:\n\nTitle: {incident.title}"
#     mail.send(msg)
# except Exception as e:
#     # Log the email error but do not crash the API
#     print("Email send failed:", e)


    return jsonify({"message": "Incident Created"}), 201


@routes.route("/incidents", methods=["GET"])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([
        {"id": i.id, "title": i.title, "status": i.status} for i in incidents
    ])


@routes.route("/incidents/<int:id>", methods=["PUT"])
def update_incident(id):
    incident = Incident.query.get(id)
    data = request.json
    incident.status = data.get("status", incident.status)
    incident.assigned_to = data.get("assigned_to", incident.assigned_to)
    db.session.commit()
    return jsonify({"message": "Incident Updated"})

