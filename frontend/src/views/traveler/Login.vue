<template>
   
  <div>
     
    <h1>PRIJAVA PUTNIKA</h1>
    <br>

    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <form @submit.prevent="loginTraveler">
            <br/>
              <b-alert class="alert-sm" variant="danger" :show="!!poruka">
                {{poruka}}
              </b-alert>
              <label><b>E-mail adresa</b></label>
              <input
                type="email"
                class="form-control"
                placeholder="Upiši email adresu"
                v-model="email"
              />
              <br/>
              <label><b>Lozinka</b></label>
              <input
                type="password"
                class="form-control"
                placeholder="Upiši lozinku"
                v-model="lozinka"
              />
              <br/>
              <button class="btn btn btn-primary mt-4">Prijavi se</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '@/store.js';
import axios from 'axios';
export default {

    data() {
    return {
      email: null,
      lozinka: null,
      store,
    }
  }, 
    methods: {
      loginTraveler() {
        axios.post('http://localhost:8000/travelers/login', {
          email: this.email,
          lozinka: this.lozinka,
         }).then((res) => {
          if(res.status === 200){
            localStorage.setItem('usertoken', res.data);
            this.store.currentTraveler = 1;
            this.email = '';
            this.lozinka = '';
            this.$router.push({ name: 'TravelerHome' });
        }
      }).catch((err) => {
        console.log(err);
      });
    },
  },
}
</script>

<style scoped>
.form-control {
  height: 55px;
  border-radius: 5px;
  margin-top:10px;
  margin-bottom:10px;
}

.btn {
  float: right;
  padding: 10px;
} 

.menu-all-place {
  padding: 1.5rem 0;
}

.menu-all-place .menu-container {
  width: 45%;
  margin: 0 auto;
}

@media (max-width: 991px) {
  .menu-all-place .menu-container {
    width: 90%;
  }
}

h1 {
  overflow: hidden;
  text-align: center;
  color: #484848;
  font-size: 22px; 
  margin-top: 70px;
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

label {
  font-family: Open Sans;
  font-style: normal;
  font-size: 15px;
  line-height: 24px;
  display: flex;
  align-items: center;
  color: #646464;
}
</style>
