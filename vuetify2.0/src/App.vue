<template>
  <v-app>
    <v-progress-linear :indeterminate="indeterminate" :style="line_style" color="green"></v-progress-linear>
    <v-content>
      <Home />
    </v-content>
  </v-app>
</template>

<script>
import Home from "./components/Home";
import { setTimeout } from "timers";

export default {
  name: "App",
  components: {
    Home
  },
  data: () => ({
    //
    indeterminate: true,
    line_style: {
      display: ""
    }
  }),
  created() {
    setTimeout(() => {
      this.indeterminate = false;
      this.line_style.display = "none";
    }, 3000);
  }
};
</script>
