<template>
  <div>
    <br><br>
    <div class="title ">
      <h1>PREGLED REZERVACIJA</h1>
    </div>
    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <div class="row">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">IME I PREZIME</th>
                  <th scope="col">E-MAIL</th>
                  <th scope="col">BROJ MOBITELA</th>
                  <th scope="col">BROJ PUTNIKA</th>
                  <th scope="col">UKUPNA CIJENA</th>
                </tr>
              </thead>
              <tbody v-for="reservation in reservations" :key="reservation.id">
                <tr>
                  <th scope="row"></th>
                  <td>{{reservation.ime}} {{reservation.prezime}} </td>
                  <td>{{reservation.email}}</td>
                  <td>{{reservation.broj_mobitela}}</td>
                  <td>{{reservation.broj_putnika}}</td>
                  <td>{{reservation.ukupna_cijena}} kn</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <br>
  </div>
        
</template>

<script>

export default {
  name: 'ReservationOverview',

  data () {

    return {
      reservations: []
    }
  },

  props: {
    id: {
      type: [Number, String],
      required: true,
    }
  },

  methods: {
    async getReservations() {
      try {
        const args = {
          method:"GET",   
          headers: {"Content-Type": "application/json"}
        }
        let response = await fetch(`http://localhost:8000/reservationse/${this.id}`, args)
        let data = await response.json()
        this.reservations.push(...data)
      } catch (error) {
          console.error(error)
        }
    }
  },

  created () {
    this.getReservations()
  }

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

.form-control {
  height: 60px;
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