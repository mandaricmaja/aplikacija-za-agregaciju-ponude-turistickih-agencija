from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


## TURISTIČKI AGENT ##
class TuristickiAgent(db.Model):

    __tablename__ = "turisticki_agent"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    naziv_turisticke_agencije = db.Column(db.String(20), nullable=False)
    broj_mobitela = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    lozinka = db.Column(db.String(20), nullable=False)

    turisticke_ponude = db.relationship('TuristickaPonuda', back_populates='turisticki_agent', lazy="dynamic")

    def __init__(self, **kwargs):
        super(TuristickiAgent, self).__init__(**kwargs)

    def serialize(self):
        return {
            'id': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'naziv_turisticke_agencije': self.naziv_turisticke_agencije,
            'broj_mobitela': self.broj_mobitela,
            'email': self.email,
            'lozinka': self.lozinka
        }


## PUTNIK ##
class Putnik(db.Model):

    __tablename__ = "putnik"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    broj_mobitela = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    lozinka = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'broj_mobitela': self.broj_mobitela,
            'email': self.email,
            'lozinka': self.lozinka
        }


## TURISTIČkA PONUDA ##
class TuristickaPonuda(db.Model):

    __tablename__ = "turisticka_ponuda"

    id = db.Column(db.Integer, primary_key=True)
    naziv_turisticke_agencije = db.Column(db.String(20), nullable=False)
    naziv_ponude = db.Column(db.String(20), nullable=False)
    lokacija = db.Column(db.String(30), nullable=False)
    mjesto_polaska = db.Column(db.String(30), nullable=False)
    datum_putovanja = db.Column(db.String(20), nullable=False)
    broj_dana = db.Column(db.String(20), nullable=False)
    cijena = db.Column(db.String(20), nullable=False)
    vrsta_prijevoza = db.Column(db.String(20), nullable=False)
    kategorija_putovanja = db.Column(db.String(20), nullable=False)
    opis_ponude = db.Column(db.String(2000), nullable=False)
    fotografija = db.Column(db.String(50), nullable=False)
    datum_objavljivanja = db.Column(db.DateTime(), default=datetime.now(), nullable=False)

    turisticki_agent_id = db.Column(db.Integer, db.ForeignKey('turisticki_agent.id'), nullable=False)

    turisticki_agent = db.relationship('TuristickiAgent', back_populates='turisticke_ponude', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'naziv_turisticke_agencije': self.naziv_turisticke_agencije,
            'naziv_ponude': self.naziv_ponude,
            'lokacija': self.lokacija,
            'mjesto_polaska': self.mjesto_polaska,
            'datum_putovanja': self.datum_putovanja,
            'broj_dana': self.broj_dana,
            'cijena': self.cijena,
            'vrsta_prijevoza': self.vrsta_prijevoza,
            'kategorija_putovanja': self.kategorija_putovanja,
            'opis_ponude': self.opis_ponude,
            'fotografija': self.fotografija,
            'datum_objavljivanja': self.datum_objavljivanja
        }


## ARHIVA ##
class Arhiva(db.Model):

    __tablename__ = "arhiva"

    id = db.Column(db.Integer, primary_key=True)
    naziv_turisticke_agencije = db.Column(db.String(20), nullable=False)
    naziv_ponude = db.Column(db.String(20), nullable=False)
    lokacija = db.Column(db.String(30), nullable=False)
    mjesto_polaska = db.Column(db.String(30), nullable=False)
    datum_putovanja = db.Column(db.String(20), nullable=False)
    broj_dana = db.Column(db.String(20), nullable=False)
    cijena = db.Column(db.String(20), nullable=False)
    vrsta_prijevoza = db.Column(db.String(20), nullable=False)
    kategorija_putovanja = db.Column(db.String(20), nullable=False)
    opis_ponude = db.Column(db.String(2000), nullable=False)
    fotografija = db.Column(db.String(50), nullable=False)
    datum_arhiviranja = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    turisticki_agent_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'naziv_turisticke_agencije': self.naziv_turisticke_agencije,
            'naziv_ponude': self.naziv_ponude,
            'lokacija': self.lokacija,
            'mjesto_polaska': self.mjesto_polaska,
            'datum_putovanja': self.datum_putovanja,
            'broj_dana': self.broj_dana,
            'cijena': self.cijena,
            'vrsta_prijevoza': self.vrsta_prijevoza,
            'kategorija_putovanja': self.kategorija_putovanja,
            'opis_ponude': self.opis_ponude,
            'fotografija': self.fotografija,
            'datum_arhiviranja': self.datum_arhiviranja,
            'turisticki_agent_id': self.turisticki_agent_id
        }

## REZERVACIJA ##
class Rezervacija(db.Model):

    __tablename__ = "rezervacija"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    broj_mobitela = db.Column(db.Integer, nullable=False)
    adresa = db.Column(db.String(120), nullable=False)
    drzava = db.Column(db.String(120), nullable=False)
    broj_putnika = db.Column(db.Integer, nullable=False)
    ukupna_cijena = db.Column(db.String(20), nullable=False)
    turisticka_ponuda_id = db.Column(db.Integer, nullable=False)
    putnik_id = db.Column(db.Integer, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'email': self.email,
            'broj_mobitela': self.broj_mobitela,
            'adresa': self.adresa,
            'drzava': self.drzava,
            'broj_putnika': self.broj_putnika,
            'ukupna_cijena': self.ukupna_cijena,
            'turisticka_ponuda_id': self.turisticka_ponuda_id,
            'putnik_id': self.putnik_id
        }

## RECENZIJA ##
class Recenzija(db.Model):

    __tablename__ = "recenzija"

    id = db.Column(db.Integer, primary_key=True)
    ocjena = db.Column(db.String(20), nullable=False)
    ukupna_ocjena = db.Column(db.String(20), nullable=False)
    komentar = db.Column(db.String(200), nullable=False)
    datum_objavljivanja = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    agent_id = db.Column(db.Integer, nullable=False)
    putnik_id = db.Column(db.Integer, nullable=False)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'ocjena': self.ocjena,
            'ukupna_ocjena': self.ukupna_ocjena,
            'komentar': self.komentar,
            'datum_objavljivanja': self.datum_objavljivanja,
            'agent_id': self.agent_id,
            'putnik_id': self.putnik_id,
            'ime': self.ime,
            'prezime': self.prezime,
        }


