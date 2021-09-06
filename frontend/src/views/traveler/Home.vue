<template>
  <div>
    <div id="hero" class="d-flex flex-column justify-content-center">
      <div class="container text-center text-md-left">
        <h2>Dobrodošli u CroTravel</h2>
        <h3>Pronađi svoju sljedeću destinaciju za putovanje!</h3>
      </div>
    </div>

    <div class="d-flex flex-column justify-content-center">
      <div class="container text-center text-md-left">
        <input
            type="search"
            class="form-control"
            placeholder="Pretraži destinaciju koju želiš posjetiti"
            v-model="search"
          /> 
      </div>
    </div>

    <div class="title">
      <h1>NAJNOVIJE PONUDE PUTOVANJA</h1>
    </div>
    
    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <div v-for="offer in filterOffers" :key="offer.id" class="col-sm-4 item-each">
              <div class="card">
                <div class="card-body">
                  <router-link :to="{name:'TravelerOfferDetails', params:{id:offer.id}}">
                    <img :src="offer.fotografija" class="fotografija" alt="fotografija" width="368" height="225">
                    <i class="bi bi-geo-alt-fill"></i>
                    <h3>{{offer.naziv_ponude}}</h3>
                    <p class="lokacija">{{offer.lokacija}}</p>
                    <p class="cijena">{{offer.cijena}}</p>
                    <i class="bi bi-calendar3"></i>
                    <p class="broj_dana">{{offer.broj_dana}}</p>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import store from '@/store.js';
import jwtDecode from 'jwt-decode';

export default {

  name: 'TravelerHome',

  data () {
    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);
    return {
      id: decoded.identity.id,
      offers: [],
      store,
      search: ''
    }
  },

  methods: {
    async getTravelOffers() {
      try {
        const args = {
          method:"GET",   
          headers: {"Content-Type": "application/json"}
        } 
        let response = await fetch ('http://localhost:8000/offers', args)
        let data = await response.json()
        this.offers.push(...data)
      } catch (error) {
          console.error(error)
        }
    }
  },
      
  created () {
    this.getTravelOffers()
  },

  computed: {
    filterOffers(){
      return this.offers.filter((offer) => {
          return offer.lokacija.toLowerCase().match(this.search.toLowerCase());
      });
    },
  }
  
}
</script>

<style scoped>
#hero {
  width: 100%;
  height: 60vh;
  background:  url('../hero.jpg');
  background-size: cover;
  position: relative;
  padding-bottom: 0;
  background-position: center;
  height: 550px;
}

#hero:before {
  content: "";
  background: rgba(104, 117, 126, 0.401);
  position: absolute;
  bottom: 0;
  top: 0;
  left: 0;
  right: 0;
}

#hero .container {
  z-index: 2;
}

#hero h2 {
  margin: 0 0 15px 0;
  font-size: 40px;
  font-weight: 700;
  line-height: 56px;
  color: #fff;
}

#hero h3 {
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 30px;
  font-size: 25px;
}

@media (max-width: 992px) {
  #hero {
    height: calc(100vh - 70px);
  }
}

@media (max-width: 768px) {
  #hero h2 {
    font-size: 30px;
    line-height: 36px;
  }
  #hero h3 {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 30px;
  }
}

.form-control {
  width: 100%;
  max-width: 255px;
  height: 55px;
  font-size: 13px;
  border-radius: 5px;
  margin-top: 25px;
  margin-bottom: 15px;
  float: right;
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
  margin: 0 auto
}

.menu-all-place .item-each {
  display: flex;
  justify-content: center;
  margin: 1rem 0;
  padding: 8px;
  transition: all .3s ease-in-out;
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

.card {
  height: 420px;
  width: 350px;
  box-shadow: 0px 0px 2px 0px #00000040;
}

.lokacija {
  max-width:100%;
  position: absolute;
  left: 16.06%;
  right: 28.94%;
  top: 59.5%;
  bottom: 26%;
  font-size: 14px;
  display: flex;
  align-items: center;
  color: #BDB9B9;
}

.card h3 {
  position: absolute;
  left: 8.45%;
  right: 36.55%;
  top: 64.75%;
  bottom: 17.75%;
  font-family: Lato;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 24px;
  display: flex;
  align-items: center;
  color: #484848;
}

.bi-geo-alt-fill {
  position: absolute;
  left: 8.45%;
  right: 87.61%;
  top: 62.0%;
  bottom: 32.25%;
  color: #BDB9B9;
  max-width: 100%;
}

.bi-calendar3 {
  position: absolute;
  width: 16px;
  height: 16px;
  left: 31px;
  top: 367px;
  color: #BDB9B9;
  max-width:100%;
}

.cijena {
  position: absolute;
  left: 72.37%;
  right: 5.63%;
  top: 88.05%;
  bottom: 4.75%;
  max-width:100%;
  font-family: Lato;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 24px;
  align-items: center;
  color: #646464;
}

.broj_dana{
  max-width:100%;
  position: absolute;
  left: 17.91%;
  right: 67.61%;
  top: 87.9%;
  bottom: 2.5%;
  font-family: Lato;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 24px;
  color: #928C8C;

}
.fotografija {
  max-width: 100%;
  position: absolute;
  right: 0px;
  top: 0px;
  filter: saturate(50%);
}
</style>