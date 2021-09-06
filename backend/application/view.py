import os,datetime
from flask import Flask, request, jsonify, json
from flask.json import JSONEncoder
from flask_cors import CORS
from datetime import datetime
from decimal import Decimal
from .model import Recenzija, TuristickiAgent, Putnik, TuristickaPonuda, Arhiva, Rezervacija, db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import desc
import uuid

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./cro-travel-db.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secret'
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    return app

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"Message": "Dobrodošli u CroTravel aplikaciju"})


## TURISTIČKI AGENT ##

# Dohvaćanje svih turističkih agenata
@app.route('/agents', methods=['GET'])
def get_travelAgents():
    travel_agents = TuristickiAgent.query.all()
    return jsonify(travel_agents)

# Dohvaćanje turističkog agenta
@app.route('/agents/<int:agent_id>', methods=['GET'])
def get_travelAgent(agent_id):
    travel_agent = TuristickiAgent.query.filter_by(id=agent_id).first()
    return jsonify(travel_agent)

# Registracija turističkog agenta
@app.route('/agents/register', methods=['POST'])
def register_travelAgent():
    data = request.get_json()
    new_travelAgent = TuristickiAgent(ime=data["ime"], prezime=data["prezime"], naziv_turisticke_agencije=data["naziv_turisticke_agencije"], broj_mobitela=data["broj_mobitela"], email=data["email"], lozinka=data["lozinka"])
    db.session.add(new_travelAgent)
    db.session.commit()
    return jsonify(new_travelAgent)

# Prijava turističkog agenta
@app.route('/agents/login', methods=['POST'])
def login_travelAgent():
    data = request.get_json()
    travel_agent = TuristickiAgent(email=data["email"], lozinka=data["lozinka"])
    rezultat = ""
    upit_email = TuristickiAgent.query.filter_by(email=travel_agent.email).first()
    upit_lozinka = TuristickiAgent.query.filter_by(lozinka=travel_agent.lozinka).first()
    if upit_email and upit_lozinka:
        access_token = create_access_token(identity ={'id': upit_email.id, 'ime': upit_email.ime, 'prezime': upit_email.prezime, 'naziv_turisticke_agencije': upit_email.naziv_turisticke_agencije, 'broj_mobitela': upit_email.broj_mobitela, 'email': upit_email.email, 'lozinka': upit_email.lozinka})
        rezultat = access_token
        return rezultat
    else:
        rezultat = jsonify({"error":"Neispravana lozinka ili email"})
        return


## TURISTIČKA PONUDA ##

# Dohvaćanje svih turističkih ponuda 
@app.route('/offers', methods=['GET'])
def get_travelOffers():
    travel_offers = TuristickaPonuda.query.order_by(desc(TuristickaPonuda.datum_objavljivanja)).limit(9).all()
    return jsonify(travel_offers)

# Dohvaćanje jedne turističke ponude
@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_travelOffer(offer_id):
    travel_offer = TuristickaPonuda.query.filter_by(id=offer_id).first()
    return jsonify(travel_offer)

# Kreiranje nove turističke ponude 
@app.route('/offers', methods=['POST'])
def post_travelOffer():
    data = request.get_json()
    new_travelAgent = TuristickaPonuda(naziv_turisticke_agencije=data["naziv_turisticke_agencije"], naziv_ponude=data["naziv_ponude"], mjesto_polaska=data["mjesto_polaska"], lokacija=data["lokacija"], datum_putovanja=data["datum_putovanja"], broj_dana=data["broj_dana"], cijena=data["cijena"], vrsta_prijevoza=data["vrsta_prijevoza"], kategorija_putovanja=data["kategorija_putovanja"], opis_ponude=data["opis_ponude"], fotografija=data["fotografija"], turisticki_agent_id=data["turisticki_agent_id"],datum_objavljivanja=datetime.now())
    db.session.add(new_travelAgent)
    db.session.commit()
    return jsonify(new_travelAgent)

# Ažuriranje određene turističke ponude 
@app.route('/offers/<int:offer_id>', methods=['PUT'])
def update_travelOffer(offer_id):
    data = request.get_json()
    offer = TuristickaPonuda.query.filter_by(id=offer_id).first()
    offer.naziv_turisticke_agencije = data["naziv_turisticke_agencije"]
    offer.naziv_ponude = data["naziv_ponude"]
    offer.mjesto_polaska = data["mjesto_polaska"]
    offer.lokacija = data["lokacija"]
    offer.datum_putovanja = data["datum_putovanja"]
    offer.broj_dana = data["broj_dana"]
    offer.cijena = data["cijena"]
    offer.vrsta_prijevoza = data["vrsta_prijevoza"]
    offer.kategorija_putovanja = data["kategorija_putovanja"]
    offer.opis_ponude = data["opis_ponude"]
    offer.fotografija = data["fotografija"]
    db.session.add(offer)
    db.session.commit()
    return jsonify(offer)

# Brisanje određene turističke ponude 
@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_travelOffer(offer_id):
    offer = TuristickaPonuda.query.filter_by(id=offer_id).first()
    db.session.delete(offer)
    db.session.commit()
    return jsonify(offer)

# Filtriranje turističkih ponuda po lokaciji
@app.route('/offers/<filter>', methods=['GET'])
def get_offerss(filter):
    qry = TuristickaPonuda.query.filter(TuristickaPonuda.lokacija == filter).all()
    return jsonify(qry)

# Filter turističkih ponuda po kategoriji putovanja
@app.route('/kategorija_putovanja/<filter>', methods=['GET'])
def get_kategorija_putovanja(filter):
    qry = TuristickaPonuda.query.filter(TuristickaPonuda.kategorija_putovanja == filter).all()
    return jsonify(qry)


## TURISTIČKA PONUDA - TURISTIČKI AGENT ##

# Dohvaćanje svih turističkih ponuda od određenog agenta
@app.route('/agents/<int:travelAgent_id>/offers', methods=['GET'])
def get_offers(travelAgent_id):
    agent = TuristickiAgent.query.filter_by(id=travelAgent_id).first()
    output = [] if agent is None else agent.turisticke_ponude.all()
    return jsonify(output)


## PUTNIK ##

# Dohvaćanje svih putnika
@app.route('/travelers', methods=['GET'])
def get_travelers():
    travelers = Putnik.query.all()
    return jsonify(travelers)

# Dohvaćanje svih putnika
@app.route('/travelers/<int:traveler_id>', methods=['GET'])
def get_traveler(traveler_id):
    traveler = Putnik.query.filter_by(id=traveler_id).first()
    return jsonify(traveler)

# Registracija turističkog agenta
@app.route('/travelers/register', methods=['POST'])
def register_traveler():
    data = request.get_json()
    new_traveler = Putnik(ime=data["ime"], prezime=data["prezime"], broj_mobitela=data["broj_mobitela"], email=data["email"], lozinka=data["lozinka"])
    db.session.add(new_traveler)
    db.session.commit()
    return jsonify(new_traveler)

# Prijava turističkog agenta
@app.route('/travelers/login', methods=['POST'])
def login_traveler():
    data = request.get_json()
    traveler = Putnik(email=data["email"], lozinka=data["lozinka"])
    rezultat = ""
    upit_email = Putnik.query.filter_by(email=traveler.email).first()
    upit_lozinka = Putnik.query.filter_by(lozinka=traveler.lozinka).first()
    if upit_email and upit_lozinka:
        access_token = create_access_token(identity ={'id': upit_email.id, 'ime': upit_email.ime, 'prezime': upit_email.prezime,'broj_mobitela': upit_email.broj_mobitela, 'email': upit_email.email, 'lozinka': upit_email.lozinka})
        rezultat = access_token
        return rezultat
    else:
        rezultat = jsonify({"error":"Neispravana lozinka ili email"})
        return 


## ARHIVA ##

# Kreiranje nove arhivirane turističke ponude
@app.route('/archive', methods=['POST'])
def post_archiveTravelOffer():
    data = request.get_json()
    arhiva = Arhiva(naziv_turisticke_agencije=data["naziv_turisticke_agencije"], naziv_ponude=data["naziv_ponude"], mjesto_polaska=data["mjesto_polaska"], lokacija=data["lokacija"], datum_putovanja=data["datum_putovanja"], broj_dana=data["broj_dana"], cijena=data["cijena"], vrsta_prijevoza=data["vrsta_prijevoza"], kategorija_putovanja=data["kategorija_putovanja"], opis_ponude=data["opis_ponude"], fotografija=data["fotografija"], turisticki_agent_id=data["turisticki_agent_id"])
    db.session.add(arhiva)
    db.session.commit()
    return jsonify(arhiva)

# Dohvaćanje arhiviranih turističkih ponuda
@app.route('/archive/<int:offer_id>', methods=['GET'])
def get_archivedTraveOffers(offer_id):
    qry = Arhiva.query.filter(Arhiva.turisticki_agent_id == offer_id).all()
    return jsonify(qry)


## REZERVACIJA ##

# Kreiranje nove rezervacije
@app.route('/reservation', methods=['POST'])
def post_reservation():
    data = request.get_json()
    rezervacija = Rezervacija(ime=data["ime"], prezime=data["prezime"], broj_mobitela=data["broj_mobitela"], email=data["email"], adresa=data["adresa"], drzava=data["drzava"], broj_putnika=data["broj_putnika"], ukupna_cijena=data["ukupna_cijena"], turisticka_ponuda_id=data["turisticka_ponuda_id"], putnik_id=data["putnik_id"])
    db.session.add(rezervacija)
    db.session.commit()
    return jsonify(rezervacija)

# Dohvaćanje rezervacija po putniku
@app.route('/reservations/<int:putnik_id>', methods=['GET'])
def get_Reservations(putnik_id):
    qry = Rezervacija.query.filter(Rezervacija.putnik_id == putnik_id).all()
    return jsonify(qry)

# Dohvaćanje rezervacija po turističkoj ponudi
@app.route('/reservationse/<int:turisticka_ponuda_id>', methods=['GET'])
def get_Reservation(turisticka_ponuda_id):
    qry = Rezervacija.query.filter(Rezervacija.turisticka_ponuda_id == turisticka_ponuda_id).all()
    return jsonify(qry)


## RECENZIJE ##

# Kreiranje nove recenzije
@app.route('/reviews', methods=['POST'])
def post_reviews():
    data = request.get_json()
    reviews = Recenzija(ime=data["ime"], prezime=data["prezime"], ocjena=data["ocjena"], ukupna_ocjena=data["ukupna_ocjena"], komentar=data["komentar"], datum_objavljivanja=datetime.now(), agent_id=data["agent_id"], putnik_id=data["putnik_id"])
    db.session.add(reviews)
    db.session.commit()
    return jsonify(reviews)

# Dohvaćanje recenzije po turističkom agentu / turističkoj agenciji
@app.route('/reviews/<int:agent_id>', methods=['GET'])
def get_Reviews(agent_id):
    qry = Recenzija.query.filter(Recenzija.agent_id == agent_id).all()
    return jsonify(qry)

# Dohvaćanje recenzija od svih turističkih agencija
@app.route('/allReviews', methods=['GET'])
def allReviews():
    allReviews = Recenzija.query.all()
    return jsonify(allReviews)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):

        if hasattr(obj, "serialize"):
          return obj.serialize()

        try:
            if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app.json_encoder = CustomJSONEncoder


if __name__ =="__main__":
  app.run(debug=True, port=8000)