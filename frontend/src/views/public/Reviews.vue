<template>

  <div>
    <div class="title">
      <h1>RECENZIJE</h1>
    </div>

    <div class="menu-all-place">
      <div class="menu-full">
        <div class="menu-container">
          <b-button class="btn btn-light" @click="getAllReviews()">Sve recenzije</b-button> 
          <b-button class="btn btn-light" v-for="agent in agents" v-bind:key="agent.id" :title="agent.naziv_turisticke_agencije" @click="getReviews(agent.id)">{{agent.naziv_turisticke_agencije}}</b-button> 
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

export default {
  
  name: 'PublicReviews',

  components: {
    StarRating,
  },

  data () {
    return {
      agents: [],
      reviews: [],
      store, 
      ocjena: '',
      komentar: '',
      ukupna_ocjena: 0,
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
  },

  created () {
    this.getAgents()
    this.getAllReviews()
  }

}
</script>

<style scoped>
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

.btn {
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
