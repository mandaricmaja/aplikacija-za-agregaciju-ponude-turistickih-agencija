<template>
   <div class="container">
      <Header  />
      <router-view/>
      <Footer />
    </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'app',
  components: {
    Header,
    Footer
  }
}
</script>

<style lang="scss">
body {
    background-color: white;
}
.bg-white {
    background-color: white;
    border-bottom: #ccc 1px solid;
    margin-bottom: 20px;
    padding: 10px;
}
nav.navbar {
    background-color: white;
    a {
        svg {
            border-right: #aaa 1px solid;
            margin-right: 10px;
            padding-right: 10px;
        }
        img {
            position: relative;
            top: 3px;
        }
    } 
}
</style>
