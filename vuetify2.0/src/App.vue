<template>
  <v-app>
    <v-progress-linear :indeterminate="indeterminate" :style="line_style" color="green"></v-progress-linear>
    <v-app-bar
      app
      elevate-on-scroll
      color="#fcb69f"
      class="animated bounceInDown"
      src="./imgs/back2_1.png"
    >
      <template v-slot:img="{ props }">
        <v-img v-bind="props"></v-img>
      </template>
      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn class="hvr-grow-shadow" text>HOME</v-btn>
        <v-btn class="hvr-grow-shadow" text>DATEFILE</v-btn>
        <v-btn class="hvr-grow-shadow" text>ABOUT</v-btn>
        <v-btn class="hvr-grow-shadow" text>CONTCTS</v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <Home />
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
