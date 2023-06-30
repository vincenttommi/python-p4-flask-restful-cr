#!/usr/bin/env python3

from faker import Faker

from app import app
from models import db, Newsletter

with app.app_context():
#is typically used  when  you need to run certain code
# within the application context,outside of the normalrequest-
#response cycle.
    fake = Faker()

    Newsletter.query.delete()
    #deletes any  data the exits in the database before fake data being seeded into
    # table

    newsletters = []
    #empty list that stores generated data
    for i in range(50):
        newsletter = Newsletter(
            title = fake.text(max_nb_chars=20),
            body = fake.paragraph(nb_sentences=5),
        )
        newsletters.append(newsletter)

    db.session.add_all(newsletters)
    # adds a collection of newletter objects  to a database session.
    
    db.session.commit()
    #committing generated data to the database
