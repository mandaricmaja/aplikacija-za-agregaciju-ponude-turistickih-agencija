<template>
  
  <div>
     <b-modal id="modal-prevent-closing" ref="modal" title="Napiši recenziju" hide-footer hide-backdrop centered close>
        <form @submit.prevent="insertTravelOffer()">
          <label><b>Turistička agencija</b></label>
          <select v-model="id_agent" class="form-control" placeholder="Odaberi turističku agenciju" id="exampleFormControlSelect1">
            <option v-for="agent in agents" v-bind:value="agent.id" v-bind:key="agent.id" :title="agent.naziv_turisticke_agencije" >{{agent.naziv_turisticke_agencije}}</option>
          </select>
          <label><b>Ocjena</b></label>
          <star-rating v-bind:star-size="30" v-model="ocjena"></star-rating>
          <br>
          <label><b>Komentar</b></label>
          <input v-model="komentar" type="text" name="name" class="form-control" id="name" placeholder="Upiši komentar" required>
          <button class="btn btn-primary btn_recenzija mt-4" @click="$bvModal.hide('modal-prevent-closing')">Dodaj recenziju</button>
          <hr>
        </form>
      </b-modal>

    <div class="title">
      <h1>RECENZIJE</h1>
    </div>

    <button v-b-modal.modal-prevent-closing class="btn btn-secondary btn_recenzija">Dodaj recenziju</button>
    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <b-button class="btn btn-light gumb" @click="getAllReviews()">Sve recenzije</b-button> 
          <b-button class="btn btn-light gumb" v-for="agent in agents" v-bind:key="agent.id" :title="agent.naziv_turisticke_agencije" @click="getReviews(agent.id)">{{agent.naziv_turisticke_agencije}}</b-button> 
          <br><br>
          <div v-for="review in reviews" :key="review.id">
          <div class="card">
              <div class="card-body">
                <p class="naziv"><b>{{review.ime}} {{review.prezime}}</b></p>
                <star-rating v-bind:star-size="15" v-model="review.ocjena" v-bind:read-only="true"></star-rating>
                <br>
                <p>{{review.komentar}}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import StarRating from 'vue-star-rating';
import store from '@/store.js';
import jwtDecode from 'jwt-decode';

export default {
  
  name: 'AgentHome',

  components: {
    StarRating,
  },

  data () {

    const token = localStorage.usertoken;
    const decoded = jwtDecode(token);

    return {
      ime: decoded.identity.ime,
      prezime: decoded.identity.prezime,
      putnik_id: decoded.identity.id,
      agents: [],
      reviews: [],
      store, 
      ocjena: '',
      komentar: '',
      ukupna_ocjena: 0,
      id_agent: '',
    }
  },

  methods: {
    async getAgents() {
      try {
        const args = {
          method:"GET",   
          headers: {"Content-Type": "application/json"}
        }
        this.agents = []
        let response = await fetch(`http://localhost:8000/agents`, args)
        let data = await response.json()
        this.agents.push(...data)
      } catch (error) {
          console.error(error)
        }
    },

    async getReviews(agent_id) {
      try {
        const args = {
          method:"GET",   
          headers: {"Content-Type": "application/json"}
        }
        this.reviews = []
        let response = await fetch(`http://localhost:8000/reviews/${agent_id}`, args)
        let data = await response.json()
        this.reviews.push(...data)
      } catch (error) {
          console.error(error)
        }
    },

  async getAllReviews() {
      try {
        const args = {
          method:"GET",   
          headers: {"Content-Type": "application/json"}
        }
           this.reviews = []
      
        let response = await fetch(`http://localhost:8000/allReviews`, args)
        let data = await response.json()
        this.reviews.push(...data)
      } catch (error) {
          console.error(error)
        }
    },

    async insertTravelOffer() {
      try {
        const args = {
          method: "POST",   
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({ocjena: this.ocjena, ukupna_ocjena: this.ukupna_ocjena, komentar: this.komentar, putnik_id: this.putnik_id, agent_id: this.id_agent, ime: this.ime, prezime: this.prezime})
      }
      let response = await fetch ('http://localhost:8000/reviews', args)
      let data = await response.json()
      this.getAllReviews()
      } catch (error) {
          console.error(error)
        }
    }
  },

  created () {
    this.getAgents()
    this.getAllReviews()
  }

}
</script>

<style scoped>
.btn_recenzija {
  float: right;
}

label {
  font-family: Open Sans;
  font-style: normal;
  font-size: 15px;
  line-height: 24px;
  display: flex;
  align-items: center;
  color: #646464;
  padding-top: 10px;
}

.form-control {
border-radius: 5px;
margin-top:10px;
margin-bottom:10px;
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

.menu-all-place {
  padding: 3rem 0;
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

.gumb {
    color: black;
    border-radius: none;
    padding: 18px;
    padding-left: 12px;
    padding-right: 12px;
    text-transform: uppercase;
    border-color: rgba(255, 255, 255, 0.8);
    margin: 2px;
    color: #484848;
}

div.card {
    width: 100%;
    height: 100%;
    margin-top: 15px;
    background: #FCFCFC;
}

.naziv {
  margin-bottom: 0px;
}

</style>
