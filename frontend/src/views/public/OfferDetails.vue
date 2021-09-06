<template>

 <div>
   <div class="menu-all-place mt-3">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <h2>{{offer.naziv_ponude}}</h2>
            <i class="bi bi-geo-alt-fill"></i>
            <p class="lokacija">{{offer.lokacija}}</p>
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
        
        <div class="title mb-5">
          <h1>PONUDA PUTOVANJA</h1>
        </div>
        
        <div class="menu-container">
          <div class="opis">
            <p>{{offer.opis_ponude}}</p>
            <p>{{offer.opis_ponude}}</p>
            <p>{{offer.opis_ponude}}</p>
          </div>
        </div>
        
      </div>
    </div>
    <br>
  </div>
   </template>

<script>

export default {

  name: 'PublicOfferDetails',

  data () {
    return {
      offer: {
      }
    }
  },

  props: {
    id: {
      type: [Number, String],
      required: true
    }
  },

  methods: {  
    async getOfferDetails() {
      try {
        const args = {
          method: "GET",   
          headers: {"Content-Type": "application/json"}
        }
        let response = await fetch(`http://localhost:8000/offers/${this.id}`, args)
        let data = await response.json()
        this.offer = data
      } catch (error) {
          console.error(error)
        }
    }
  },
           
  created() {
    this.getOfferDetails()
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