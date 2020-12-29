from models import db, Pet
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name='Foxy', speacies='Dog', photo='https://images.unsplash.com/photo-1534551767192-78b8dd45b51b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', age=3, notes='Well behaved')
p2 = Pet(name='Skyp', speacies='Dog', photo='https://images.unsplash.com/photo-1554456854-55a089fd4cb2?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', age=5, notes='Loves Walks')
p3 = Pet(name='Onix', speacies='Dog', photo='https://images.unsplash.com/photo-1560830672-575980201c33?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80', age=2, notes='Lazy')
p4 = Pet(name='Pippo', speacies='Dog', photo='https://images.unsplash.com/photo-1550953581-a75aa86fec20?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80', age=6, notes='Sleepyng alot')
p5 = Pet(name='Champ', speacies='Dog', photo='https://images.unsplash.com/photo-1529429617124-95b109e86bb8?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=675&q=80', age=1, notes='Bad Boy')
p6 = Pet(name='Leo', speacies='Dog', photo='https://images.unsplash.com/photo-1530281700549-e82e7bf110d6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80', age=9, notes='Well behaved')
p7 = Pet(name='Lady', speacies='Dog', photo='https://images.unsplash.com/photo-1547407139-3c921a66005c?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80', age=8, notes='Funny')

db.session.add_all([p1,p2,p3,p4,p5,p6,p7])
db.session.commit()

