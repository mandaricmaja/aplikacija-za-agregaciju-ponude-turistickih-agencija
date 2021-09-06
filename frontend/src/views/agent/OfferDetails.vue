<template>
<div>
  <div class="menu-all-place">
    <div class="menu-full">
      <div class="menu-container">
        <div class="row">
          <div class="col-lg-6">
            <h2>{{offer.naziv_ponude}}</h2>
            <i class="bi bi-geo-alt-fill"></i>
            <p class="lokacija">{{offer.lokacija}}</p>
          </div>
          <div class="col-lg-6">
            <div class="gumb"/>
              <router-link
                :to="{name:'AgentEditOffer', params:{id:offer.id}}"
                class="btn btn-secondary mt-3">
                Izmijeni
              </router-link>
              <button class="btn btn-secondary mx-3 mt-3" @click="insertTravelOffer(offer); deleteOffer()">Arhiviraj</button>
            </div>
          </div>
        </div>
      </div>

      <div class="title">
        <h1>OSNOVNE INFORMACIJE</h1>
        <br>
      </div>

      <div class="menu-container">
        <div class="row">
          <div class="col-lg-6">
            <p class="datum"><b>Datum: </b>{{offer.datum_putovanja}}</p>
            <p class="naziv_agencije"><b>Naziv turističke agencije: </b>{{offer.naziv_turisticke_agencije}}</p>
            <p class="mjesto_polaska"><b>Mjesto polaska: </b>{{offer.mjesto_polaska}}</p>
            <p class="broj_dana"><b>Broj dana: </b>{{offer.broj_dana}}</p>
            <p class="cijena"><b>Cijena: </b>{{offer.cijena}}</p>
            <p class="vrsta_prijevoza"><b>Vrsta prijevoza: </b>{{offer.vrsta_prijevoza}}</p>
          </div>
          <div class="col-lg-6">
            <img :src="offer.fotografija" class="fotografija" alt="Paris">
          </div>
        </div>
        <br><br>
      </div>
        
      <div class="title">
        <h1>OPIS TURISTIČKE PONUDE</h1>
        <br><br>
      </div>
        
      <div class="menu-container">
        <div class="opis">
          <p>{{offer.opis_ponude}}</p>
          <p>{{offer.opis_ponude}}</p>
          <p>{{offer.opis_ponude}}</p>
        </div>
      </div>
      <br>
      <hr>

      <div class="menu-container">
        <div class="opis">
          <router-link
          :to="{name:'AgentReservationOverview', params:{id:offer.id}}"
          class="btn btn-primary mt-3"
          >Pregled rezervacija
          </router-link>
          <br>
        </div>
      </div>
      <br>
    </div>
  </div>

</template>


<script>
import store from '@/store.js';
import jwtDecode from 'jwt-decode';

export default {
    
  name: 'AgentOfferDetails',
    
  data () {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);

    return {
      id_agent: decoded.identity.id,
      offers: [],
      store,
      offer:{
      },
      Arhiva: {
        naziv_turisticke_agencije: null,
        naziv_ponude: null,
        mjesto_polaska: null,
        lokacija: null,
        datum_putovanja: null,
        broj_dana: null,
        cijena: null,
        vrsta_prijevoza: null,
        kategorija_putovanja: null,
        opis_ponude: null,
        fotografija: null
      },
    }
  },

  props: {
    id: {
    type: [Number, String],
    required: true
    }
  },

  methods: {  

    async insertTravelOffer(ArhivaID) {
      this.Arhiva = ArhivaID;
      try {
        const args = {
        
          method: "POST",   
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
          naziv_turisticke_agencije: this.Arhiva.naziv_turisticke_agencije, 
          mjesto_polaska: this.Arhiva.mjesto_polaska,
          naziv_ponude: this.Arhiva.naziv_ponude, 
          lokacija: this.Arhiva.lokacija, 
          datum_putovanja: this.Arhiva.datum_putovanja, 
          broj_dana: this.Arhiva.broj_dana, 
          cijena: this.Arhiva.cijena, 
          vrsta_prijevoza: this.Arhiva.vrsta_prijevoza,
          kategorija_putovanja: this.Arhiva.kategorija_putovanja, 
          opis_ponude: this.Arhiva.opis_ponude, 
          fotografija: this.Arhiva.fotografija, 
          turisticki_agent_id: this.id_agent})
      }
      let response = await fetch ('http://localhost:8000/archive', args)
      let data = await response.json()
      this.$router.push({name: 'AgentHome'})
      } catch (error) {
          console.error(error)
        }
    },

        deleteOffer(){
            fetch(`http://localhost:8000/offers/${this.id}`, {
                method:"DELETE",   
                headers: {
                "Content-Type": "application/json"
                }
            })
            .then(data => {
                this.$router.push({
          name: 'AgentHome'
        })
            })
            .catch(console => {
                console.log(error)
            })
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
    }
}

</script>
<style scoped>

.btn {
  float: right
}

.menu-all-place {
  padding: 1.5rem 0;
}

.menu-all-place .menu-container {
  width: 85%;
  margin: 0 auto;
}

@media (max-width: 991px) {
  .menu-all-place .menu-container {
    width: 90%;
  }
}

.bi-geo-alt-fill {
  position: relative;
  top: 13px;
  color: #BDB9B9;
}

.lokacija {
  max-width:100%;
  position: relative;
  left: 25px;
  bottom: 8px;
  color: #BDB9B9;
}

.datum {
  position: relative;
  top: 30px; 
}

.naziv_agencije {
  position: relative;
  top: 50px;
}

.mjesto_polaska {
  position: relative;
  top: 70px;
}

.broj_dana {
  position: relative;
  top: 90px;
}

.cijena {
  position: relative;
  top: 110px;
}

.vrsta_prijevoza {
  position: relative;
  top: 130px;
} 

.fotografija {
  max-width: 100%;
  filter: saturate(50%);
  height: auto;
  float: right;
  width:  460px;
  height: 330px;
  object-fit: cover;
  margin-top: 25px;
}

.opis {
  text-align: justify;
  text-justify: inter-word;
  
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
</style>
