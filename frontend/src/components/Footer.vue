<template>
<div>
  <!-- ======= Top Bar ======= -->
  <section id="topbar" class="d-flex align-items-center">
    <div class="container d-flex justify-content-center justify-content-md-between">
      <div class="social-links d-none d-md-flex align-items-center">
        <a href="#" class="facebook"><i class="bi bi-facebook"></i></a>
        <a href="#" class="twitter"><i class="bi bi-twitter"></i></a>
        <a href="#" class="instagram"><i class="bi bi-instagram"></i></a>
      </div>
      <div v-if="store.currentUser == 0 && store.currentTraveler == 0" class="contact-info d-flex align-items-center">
         <router-link class="nav-item nav-link" to="/agent/login" style="color: #E3E0E0;">Prijava turističkog agenta</router-link>
      <router-link class="nav-item nav-link" to="/agent/register" style="color: #E3E0E0;">Registracija turističkog agenta</router-link>
      </div>
      
    </div>
  </section>
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


/*--------------------------------------------------------------
# Top Bar
--------------------------------------------------------------*/
#topbar {
  background: #686D6E;
  padding: 10px 0;
  font-size: 14px;
}

#topbar .contact-info i {
  font-style: normal;
  color: #f03c02;
}

#topbar .contact-info i a, #topbar .contact-info i span {
  padding-left: 5px;
  color: #2b2320;
}

#topbar .contact-info i a {
  line-height: 0;
  transition: 0.3s;
}

.social-links a {
  color: #E3E0E0;;
  line-height: 0;
  transition: 0.3s;
  margin-left: 15px;

}
</style>