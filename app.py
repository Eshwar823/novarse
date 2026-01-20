import os
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


class ServiceCategory:
    """Simple container for service category information."""

    def __init__(self, slug, title, short_desc, long_desc, detail, image):
        self.slug = slug
        self.title = title
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.detail = detail
        self.image = image


services = [
    ServiceCategory(
        slug="construction",
        title="Construction & Real Estate",
        short_desc="Innovative IT solutions for building the spaces where we live and work.",
        long_desc=(
            "We provide technology services that help construction and real estate firms "
            "plan, design and manage projects more efficiently. Our tools improve collaboration "
            "and visibility across all phases of development."
        ),
        detail=(
            "The construction and real estate sectors shape communities and drive economic "
            "growth. Our solutions support everything from green building practices to property "
            "management. We help clients leverage data and modern software to build and manage "
            "infrastructure, homes and commercial spaces more sustainably."
        ),
        image="construction.png",
    ),
    ServiceCategory(
        slug="healthcare",
        title="Healthcare Industry",
        short_desc="Technology‑driven solutions to enhance patient care and efficiency.",
        long_desc=(
            "Healthcare organizations need secure, scalable platforms. We develop applications "
            "that streamline operations, protect sensitive data and improve patient outcomes."
        ),
        detail=(
            "From electronic health records to telemedicine platforms, we design systems "
            "that help providers deliver high‑quality care. Our solutions leverage AI and data "
            "analytics to inform decision making and personalize treatment plans."
        ),
        image="healthcare.png",
    ),
    ServiceCategory(
        slug="banking",
        title="Banking & Financial",
        short_desc="Secure and scalable systems for the financial sector.",
        long_desc=(
            "Financial institutions trust us to build reliable platforms that handle transactions "
            "safely and efficiently. We integrate compliance, risk management and analytics into "
            "every solution."
        ),
        detail=(
            "Our services enable banks and fintech companies to modernize legacy systems, "
            "automate processes and meet regulatory requirements. We focus on security, "
            "scalability and user experience to drive growth in a competitive market."
        ),
        image="banking.png",
    ),
    ServiceCategory(
        slug="retail",
        title="Retail Industry",
        short_desc="Cutting‑edge technology to enhance the shopping experience.",
        long_desc=(
            "Retailers rely on digital platforms to engage customers. Our solutions combine e‑commerce, "
            "inventory management and analytics to create seamless shopping experiences."
        ),
        detail=(
            "We help retailers harness omnichannel strategies, optimize supply chains and personalize "
            "marketing. Our expertise in mobile and web development ensures your store is wherever "
            "your customers are."
        ),
        image="retail.png",
    ),
    ServiceCategory(
        slug="manufacturing",
        title="Manufacture Industry",
        short_desc="Driving industrial innovation with advanced technology.",
        long_desc=(
            "Manufacturers benefit from automation and data analytics. We deploy solutions that improve "
            "productivity and quality across the production lifecycle."
        ),
        detail=(
            "Our systems integrate IoT devices, sensors and machine learning to monitor equipment and "
            "predict maintenance needs. By digitizing workflows, we help factories become smarter and "
            "more efficient."
        ),
        image="manufacturing.png",
    ),
    ServiceCategory(
        slug="oil_gas",
        title="Oil & Gas Industry",
        short_desc="Optimizing energy resources with intelligent solutions.",
        long_desc=(
            "Energy companies face complex challenges from exploration to distribution. Our tools support "
            "decision making, safety and environmental compliance."
        ),
        detail=(
            "We provide data platforms that integrate field data, geological models and predictive analytics. "
            "Our solutions help clients reduce downtime, manage assets and operate sustainably in the oil "
            "and gas sector."
        ),
        image="oil_gas.png",
    ),
    ServiceCategory(
        slug="service",
        title="Service Industry",
        short_desc="Customized strategies to empower service excellence.",
        long_desc=(
            "Businesses in the service sector rely on customer relationships. We build systems that enhance "
            "communication, scheduling and customer satisfaction."
        ),
        detail=(
            "Our solutions support hospitality, consulting and other service providers with appointment booking, "
            "CRM integration and workflow automation. We tailor technology to fit your unique processes."
        ),
        image="hero.png",
    ),
]


jobs = [
    {
        "title": "Programmer Analyst",
        "salary": "$120,000 per year",
        "type": "Full‑time",
        "date_posted": "06/25/2025",
        "duties": [
            "Write and analyze programs using modern languages and frameworks.",
            "Retrieve and store data efficiently using SQL databases.",
            "Develop web interfaces with HTML5, JavaScript and CSS frameworks.",
            "Collaborate with teams across multiple environments.",
        ],
        "qualifications": [
            "Bachelor's degree in Computer Science or related field.",
            "Experience with at least one modern programming language.",
            "Familiarity with front‑end technologies such as Angular or React.",
            "Willingness to travel to client sites if required.",
        ],
        "contact": "Send your resume to careers@example.com",
    },
    {
        "title": "Software Developer",
        "salary": "$140,000 per year",
        "type": "Full‑time",
        "date_posted": "06/25/2025",
        "duties": [
            "Design and implement cloud‑based applications.",
            "Conduct code reviews and refactor existing components.",
            "Collaborate on DevOps practices and continuous integration.",
            "Stay current with emerging technologies and frameworks.",
        ],
        "qualifications": [
            "Master's degree or equivalent experience in Computer Science.",
            "Proficiency in Java, C# or similar languages.",
            "Experience with AWS or Azure cloud platforms.",
            "Strong understanding of software development lifecycles.",
        ],
        "contact": "Send your resume to careers@example.com",
    },
    {
        "title": "Project Manager",
        "salary": "$130,000 per year",
        "type": "Full‑time",
        "date_posted": "06/25/2025",
        "duties": [
            "Oversee project timelines, budgets and deliverables.",
            "Coordinate cross‑functional teams to achieve project goals.",
            "Ensure compliance with contractual obligations and standards.",
            "Communicate progress and risks to stakeholders.",
        ],
        "qualifications": [
            "Bachelor's degree in Business or Engineering.",
            "Experience managing software or construction projects.",
            "Strong leadership and communication skills.",
            "PMP certification is a plus.",
        ],
        "contact": "Send your resume to careers@example.com",
    },
]


@app.context_processor
def inject_globals():
    """Inject common variables into all templates."""
    return {
        "categories": services,
        "current_year": datetime.utcnow().year,
    }


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html", title="About")


@app.route("/services")
def services_page():
    """Render the services overview page."""
    return render_template("services.html", title="Services")


@app.route("/services/<slug>")
def service_detail(slug):
    """Render a specific service detail page."""
    category = next((s for s in services if s.slug == slug), None)
    if category is None:
        return render_template("not_found.html", message="Service not found"), 404
    return render_template("service_detail.html", title=category.title, category=category)


@app.route("/careers")
def careers():
    """Render the careers page."""
    return render_template("careers.html", title="Careers", jobs=jobs)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Render and process the contact form."""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        subject = request.form.get("subject")
        message = request.form.get("message")
        # Append the message to a local file for demonstration. In production, you
        # would likely send an email or store this data in a database.
        with open("contact_messages.txt", "a", encoding="utf-8") as f:
            f.write(
                f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}\n---\n"
            )
        return render_template("contact.html", title="Contact", success=True)
    return render_template("contact.html", title="Contact", success=False)


@app.errorhandler(404)
def page_not_found(error):
    """Render a custom 404 page."""
    return render_template("not_found.html", message="Page not found"), 404


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
