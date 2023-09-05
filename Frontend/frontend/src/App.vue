<template>
  <div id="app">
    <b-row>
      <b-col>
        <navbar/>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <router-view/>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar';

export default {
    name: 'App',
    components: { Navbar }
};
</script>

