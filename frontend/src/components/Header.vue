<template>

<div class="bg-white">
  <div class="container">
    <div class="row">
      <div class="col">

        <nav v-if="store.currentUser == 0 && store.currentTraveler == 0"  class="navbar navbar-expand-lg navbar-light">
          <router-link class="navbar-brand" :to="{ name: 'PublicHome' }">
            <img src="@/assets/cro-travel.png" width="100" />
          </router-link>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
            >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <div class="navbar-nav ms-auto">
              <router-link class="nav-item nav-link" to="/">Naslovnica</router-link>
              <router-link class="nav-item nav-link" to="/public/traveloffers">Ponude putovanja</router-link>
              <router-link class="nav-item nav-link" to="/public/reviews">Recenzije</router-link>
              <router-link class="nav-item nav-link" to="/traveler/login">Prijava putnika</router-link>
              <router-link class="nav-item nav-link" to="/traveler/register">Registracija putnika</router-link>
            </div>
          </div>
        </nav>

         <nav v-if="store.currentUser == 1" class="navbar navbar-expand-lg navbar-light">
          <router-link class="navbar-brand" :to="{ name: 'AgentHome' }">
            <img src="@/assets/cro-travel.png" width="100" />
          </router-link>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
            >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <div class="navbar-nav ms-auto">
              <router-link class="nav-item nav-link" to="/agent/home">Naslovnica</router-link>
              <router-link class="nav-item nav-link" to="/agent/newoffer">Dodaj turističku ponudu</router-link>
              <router-link class="nav-item nav-link" to="/agent/archive">Arhiva</router-link>
              <router-link class="nav-item nav-link" to="/agent/reviews">Recenzije</router-link>
              <a @click="logoutAgent" class="nav-item nav-link">Odjava</a>
            </div>
          </div>
        </nav>

        <nav v-if="store.currentTraveler == 1"  class="navbar navbar-expand-lg navbar-light">
          <router-link class="navbar-brand" :to="{ name: 'TravelerHome' }">
            <img src="@/assets/cro-travel.png" width="100" />
          </router-link>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
            >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <div class="navbar-nav ms-auto">
              <router-link class="nav-item nav-link" to="/traveler/home">Naslovnica</router-link>
               <router-link class="nav-item nav-link" to="/traveler/traveloffers">Ponude putovanja</router-link>
               <router-link class="nav-item nav-link" to="/traveler/reviews">Recenzije</router-link>
              <a @click="logoutTraveler" class="nav-item nav-link">Odjava</a>
            </div>
          </div>
        </nav>
        
      </div>
    </div>
  </div>
</div>

</template>


<script>
import store from '@/store.js';

export default {

  data () {
    return {
      store
    }
  },

  methods: {
    logoutAgent() {
      localStorage.removeItem('usertoken');
      this.$router.push({ name: 'PublicHome' });
      this.store.currentUser = 0;
      console.log(store.currentUser)
    },
    logoutTraveler() {
      localStorage.removeItem('usertoken');
      this.$router.push({ name: 'PublicHome' });
      this.store.currentTraveler = 0;
      console.log(store.currentTraveler)
    },
  }

}
</script>


<style scoped>
nav.navbar a img {
    position: relative;
    top: 0px;
}
</style>