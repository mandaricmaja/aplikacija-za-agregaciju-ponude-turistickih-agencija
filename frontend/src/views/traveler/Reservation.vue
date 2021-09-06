<template>
  <div>
    <br><br>
    <div class="title ">
      <h1>OSOBNE INFORMACIJE</h1>
    </div>

    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <form @submit.prevent="insertReservation" role="form" class="php-email-form">
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Ime</b></label>
                  <input v-model="ime" type="text" name="name" class="form-control" id="name" placeholder="Upiši ime" required>
                </div>
                <div class="col-md-6 form-group mt-3 ">
                  <label><b>Prezime</b></label>
                  <input v-model="prezime" type="text" class="form-control" name="email" id="email" placeholder="Upiši prezime" required>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  
                  <label><b>Email-adresa</b></label>
                  <input v-model="email" type="email" name="name" class="form-control" id="name" placeholder="Upiši e-mail adresu" required>
                </div>
                <div class="col-md-6 form-group mt-3">
                  <label><b>Broj mobitela</b></label>
                  <input v-model="broj_mobitela" type="text" class="form-control" name="email" id="email" placeholder="Upiši broj mobitela" required>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Adresa</b></label>
                  <input v-model="adresa" type="text" name="name" class="form-control" id="name" placeholder="Upiši adresu" required>
                </div>
                <div class="col-md-6 form-group mt-3">
                  <label><b>Država</b></label>
                  <input v-model="drzava" type="text" class="form-control" name="email" id="email" placeholder="Upiši državu" required>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <br>

    <div class="title">
      <h1>PUTNE INFORMACIJE</h1>
    </div>

    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <form role="form" class="php-email-form">
              <div class="col-md-6 form-group mt-3">
                <label><b>Broj putnika</b></label>
                <input v-model="broj_putnika" type="text" name="name" class="form-control" id="name" placeholder="Upiši broj putnika" required>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <br>

    <div class="title">
      <h1>DETALJI REZERVACIJE</h1>
    </div>

    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <div class="card mb-3" style="max-width: 100%;">
              <div class="row no-gutters">
                <div class="col-md-6">
                  <img :src="offer.fotografija" class="fotografija" alt="Paris" width="500" height="380">
                </div>
                <div class="col-md-6">
                  <div class="card-body">
                    <h5 class="card-title">{{offer.naziv_ponude}}</h5>
                    <p class="card-text">{{offer.lokacija}}</p>
                    <p class="card-text"><b>Datum: </b>{{offer.datum_putovanja}}</p>
                    <p class="card-text"><b>Broj putnika: </b>{{broj_putnika}}</p>
                    <p class="card-text"><b>Cijena: </b>{{offer.cijena}}</p>
                    <p class="card-text"><b>Ukupno: </b>{{cijena=parseInt(offer.cijena)* broj_putnika}}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button class="btn btn-primary mt-4" @click="insertReservation(cijena)">Rezerviraj</button>
    </div>
    <br>
    <hr>
</div>
</template>

<script>
import jwtDecode from 'jwt-decode';

export default {
   name: 'Reservation',
  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      putnik_id: decoded.identity.id,
      ime: decoded.identity.ime,
      offer:{},
      prezime: decoded.identity.prezime,
      email: decoded.identity.email,
      broj_mobitela: decoded.identity.broj_mobitela,
      adresa: null,
      drzava: null,
      broj_putnika: null,
    }
  }, 

  props: {
    id: {
      type: [Number, String],
      required: true,
    }
  },

  methods: {
    async insertReservation(ukupnaCijena) {
      try {
        const args = {
          method: "POST",   
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({ime: this.ime, prezime: this.prezime, email: this.email, broj_mobitela: this.broj_mobitela, adresa: this.adresa, drzava: this.drzava, broj_putnika: this.broj_putnika, ukupna_cijena: ukupnaCijena, turisticka_ponuda_id: this.id, putnik_id: this.putnik_id})
      }
      let response = await fetch ('http://localhost:8000/reservation', args)
      let data = await response.json()
      this.$router.push({name: 'TravelerHome'})
      } catch (error) {
          console.error(error)
        }
    },
         
  getOfferData() {
    fetch(`http://localhost:8000/offers/${this.id}`, {
        method:"GET",   
        headers: {
        "Content-Type": "application/json"
        }
    })
    .then(resp => resp.json())
    .then(data => {
        this.offer = data
    })
    .catch(console => {
        console.log(error)
    })
    }
    },
    created() {
            this.getOfferData()
    },
}

</script>

<style scoped>
.card-title {
  padding-top: 10px;
}

.card-text {
  padding-top: 20px;
}

.btn {
  float: right
} 

.fotografija {
  max-width: 100%;
  filter: saturate(70%);
  padding: 10px 0;
}

h1 {
  overflow: hidden;
  text-align: center;
  color: #484848;
  font-size: 22px; 
}

h1:before,
h1:after {
  background-color: #D8D3D3;
  content: "";
  display: inline-block;
  height: 1px;
  position: relative;
  vertical-align: middle;
  width: 50%;
}

h1:before {
  right: 2.5em;
  margin-left: -50%;
}

h1:after {
  left: 2.5em;
  margin-right: -50%;
} 
.menu-all-place {
  padding: 3rem 0;
}

.menu-all-place .menu-container {
  width: 85%;
  margin: 0 auto;
}


.menu-all-place .item-each:hover {
  transform: translateY(-5px);
}

@media (min-width: 1570px) {
  .menu-all-place .item-each:hover {
    box-shadow: none;
  }
}

@media (max-width: 991px) {
  .menu-all-place .menu-container {
    width: 90%;
  }
}

@media (max-width: 575px) {
  .hero-all-place .all-place-heading {
    padding: 8rem 0 6rem;
    font-size: 24px;
  }
  .menu-all-place .item-each {
    text-align: center;
    margin: 0;
  }
}

@media (max-width: 360px) {
  .hero-all-place .all-place-heading span {
    padding: 8px 14px;
  }
}

@media (max-width: 320px) {
  .hero-all-place .all-place-heading {
    font-size: 18px;
  }
}
.form-control{
  height: 55px;
  width: 525px;
  border-radius: 5px;
  margin-top:10px;
  margin-bottom:10px;
}

label {
  font-family: Open Sans;
  font-style: normal;
  font-size: 15px;
  line-height: 24px;
  display: flex;
  align-items: center;
  color: #646464;
}

.contact .php-email-form {
  width: 100%;
}

.contact .php-email-form .form-group {
  padding-bottom: 8px;
}

@-webkit-keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
