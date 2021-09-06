import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'PublicHome',
    component: () => import('../views/public/Home.vue'),
  }, 
  
  {
    path: '/offers/:id',
    name: 'PublicOfferDetails',
    component: () => import('../views/public/OfferDetails.vue'),
    props: true
  }, 

  {
    path: '/public/traveloffers',
    name: 'PublicTravelOffers',
    component: () => import('../views/public/TravelOffers.vue'),
  },

  {
    path: '/public/reviews',
    name: 'PublicReviews',
    component: () => import('../views/public/Reviews.vue'),
  },

  {
    path: '/agent/login',
    name: 'AgentLogin',
    component: () => import('../views/agent/Login.vue')
  }, 

  {
    path: '/agent/register',
    name: 'AgentRegister',
    component: () => import('../views/agent/Register.vue')
  }, 

  {
    path: '/agent/home',
    name: 'AgentHome',
    component: () => import('../views/agent/Home.vue')
  }, 

  {
    path: '/agent/offers/:id',
    name: 'AgentOfferDetails',
    component: () => import('../views/agent/OfferDetails.vue'),
    props: true
  },

  {
    path: '/agent/newoffer',
    name: 'AgentNewOffer',
    component: () => import('../views/agent/NewOffer.vue')
  }, 

  {
    path: '/agent/edit/:id',
    name: 'AgentEditOffer',
    component: () => import('../views/agent/EditOffer.vue'),
    props: true
  },

  {
    path: '/agent/reviews',
    name: 'AgentReviews',
    component: () => import('../views/agent/Reviews.vue'),
  },

  {
    path: '/agent/archive',
    name: 'AgentArchive',
    component: () => import('../views/agent/Archive.vue')
  },

  {
    path: '/overview/:id',
    name: 'AgentReservationOverview',
    component: () => import('../views/agent/ReservationOverview.vue'),
    props: true
  },

  {
    path: '/traveler/login',
    name: 'TravelerLogin',
    component: () => import('../views/traveler/Login.vue')
  }, 

  {
    path: '/traveler/register',
    name: 'TravelerRegister',
    component: () => import('../views/traveler/Register.vue')
  },
 
  {
    path: '/traveler/home',
    name: 'TravelerHome',
    component: () => import('../views/traveler/Home.vue'),
  },

  {
    path: '/traveler/offers/:id',
    name: 'TravelerOfferDetails',
    component: () => import('../views/traveler/OfferDetails.vue'),
    props: true
  },

  {
    path: '/traveler/traveloffers',
    name: 'TravelerTravelOffers',
    component: () => import('../views/traveler/TravelOffers.vue'),
  },

  {
    path: '/traveler/reviews',
    name: 'TravelerReviews',
    component: () => import('../views/traveler/Reviews.vue'),
  },

  {
    path: '/traveler/reservation/:id',
    name: 'TravelerReservation',
    component: () => import('../views/traveler/Reservation.vue'),
    props: true
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
