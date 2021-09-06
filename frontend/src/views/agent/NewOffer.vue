<template>

  <div>
    <br><br>
    <div class="title ">
      <h1>DODAJ NOVU PONUDU</h1>
    </div>
     <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <form @submit.prevent="insertTravelOffer" role="form" class="php-email-form">
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Naziv ponude</b></label>
                  <input v-model="naziv_ponude" type="text" name="name" class="form-control" id="name" placeholder="Upiši naziv ponude" required>
                </div>
                <div class="col-md-6 form-group mt-3 ">
                  <label><b>Lokacija</b></label>
                  <input v-model="lokacija" type="text" class="form-control" name="email" id="email" placeholder="Upiši lokaciju" required>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Naziv turističke agencije</b></label>
                  <input v-model="naziv_turisticke_agencije" type="text" name="name" class="form-control" id="name" placeholder="Upiši naziv turističke agencije" required>
                </div>
                <div class="col-md-6 form-group mt-3">
                  <label><b>Datum putovanja</b></label>
                  <input v-model="datum_putovanja" type="text" class="form-control" name="email" id="email" placeholder="Upiši datum putovanja" required>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Mjesto polaska</b></label>
                  <input v-model="mjesto_polaska" type="text" name="name" class="form-control" id="name" placeholder="Upiši mjesto polaska" required>
                </div>
                <div class="col-md-6 form-group mt-3">
                  <label><b>Broj dana</b></label>
                  <input v-model="broj_dana" type="text" class="form-control" name="email" id="email" placeholder="Upiši broj dana" required>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Cijena</b></label>
                  <input v-model="cijena" type="text" name="name" class="form-control" id="name" placeholder="Upiši cijenu" required>
                </div>
                <div class="col-md-6 form-group mt-3">
                  <label><b>Vrsta prijevoza</b></label>
                  <select v-model="vrsta_prijevoza" class="form-control" placeholder="Odaberi vrstu prijevoza" id="exampleFormControlSelect1">
                    <option>Avion</option>
                    <option>Autobus</option>
                    <option>Brod</option>
                  </select>
                </div>
              </div> 
              <div class="row">
                <div class="col-md-6 form-group mt-3">
                  <label><b>Vrsta putovanja</b></label>
                  <select v-model="kategorija_putovanja" class="form-control" id="exampleFormControlSelect1">
                    <option>First Minute</option>
                    <option>Jednodnevni</option>
                    <option>Hrvatska putovanja</option>
                    <option>Europska putovanja</option>
                    <option>Daleka putovanja</option>
                    <option>Krstarenja</option>
                  </select>
                </div>
                <div class="col-md-6 form-group mt-3">
                  <label><b>Fotografija</b></label>
                  <input v-model="fotografija" type="text" name="name" class="form-control" id="name" placeholder="Odaberi fotografiju" required>
                </div>
                </div>
              <div class="row">
                <div class="col-md-12 mt-3">
                 <label><b>Opis ponude</b></label>
                <textarea v-model="opis_ponude" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
              </div>
              </div>
              <button class="btn btn-primary mt-4">Dodaj ponudu</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>

</template>

<script>
import jwtDecode from 'jwt-decode';

export default {
  name: 'AgentLogin',

  data() {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      id: decoded.identity.id,
      naziv_ponude: null,
      lokacija: null,
      datum_putovanja: null,
      broj_dana: null,
      cijena: null,
      vrsta_prijevoza: null,
      kategorija_putovanja: null,
      opis_ponude: null,
      fotografija: null,
      naziv_turisticke_agencije: null,
      mjesto_polaska: null
    }
  }, 

  methods: {
    async insertTravelOffer() {
      try {
        const args = {
          method: "POST",   
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({naziv_ponude: this.naziv_ponude, naziv_turisticke_agencije: this.naziv_turisticke_agencije, mjesto_polaska: this.mjesto_polaska, lokacija: this.lokacija, datum_putovanja: this.datum_putovanja, broj_dana: this.broj_dana, cijena: this.cijena, vrsta_prijevoza: this.vrsta_prijevoza, kategorija_putovanja: this.kategorija_putovanja, opis_ponude: this.opis_ponude, fotografija: this.fotografija, turisticki_agent_id: this.id})
      }
      let response = await fetch ('http://localhost:8000/offers', args)
      let data = await response.json()
      this.$router.push({name: 'AgentHome'})
      } catch (error) {
          console.error(error)
        }
    }
  }  
}
</script>

<style scoped>
.card-title{
  padding-top: 10px;
}

.card-text{
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

label{
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