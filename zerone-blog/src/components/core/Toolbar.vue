<template>
  <!-- <v-img src="../../imgs/back3_1.png" class="first">  class="first" -->
  <div :style="toolbar_style">
    <v-app-bar
      fixed
      elevate-on-scroll
      :color="appbarColor"
      height="80"
      class="animated slideInDown"
    >
      <v-app-bar-nav-icon class="hidden-md-and-up" @click="toggleDrawer"></v-app-bar-nav-icon>

      <v-btn class="hvr-bounce-in" text color="white" to="/">
        <v-icon>mdi-home</v-icon>
      </v-btn>

      <!-- <template v-slot:color="{ props }">
        <v-app-bar v-bind="props" gradient="to top right, rgba(55,236,186,.7), rgba(25,32,72,.7)"></v-app-bar>
      </template>-->

      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn class="hvr-bounce-in" text dark to="/article">DATEFILE</v-btn>

        <v-btn class="hvr-bounce-in" text dark to="/about">ABOUT</v-btn>

        <v-btn class="hvr-bounce-in" text dark>CONTECTS</v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-container class="my-9" justify-center>
      <v-layout>
        <v-flex xs12 md12 lg12 class="text-center my-9">
          <v-avatar size="90" class="my-0 animated jackInTheBox hvr-icon-pulse">
            <img src="../../imgs/avatar.jpeg" class="hvr-icon" alt="avatar" />
          </v-avatar>
          <h2 class="white--text mb-2 display-0 text-xs-center">Personal Blog</h2>
          <div class="subheading mb-2 text-xs-center">Powered by Zerone</div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
  <!-- </v-img> -->
</template>
<script>
import { mapMutations } from "vuex";

export default {
  data: () => ({
    appbarColor: "transparent",
    toolbar_style: {
      backgroundImage: "url(" + require("../../imgs/toolbar.png") + ")",
      height: "300px",
      width: "100%",
      backgroundSize: "cover",
      backgroundRepeat: "no-repeat"
    }
  }),
  methods: {
    ...mapMutations(["toggleDrawer"]),
    changeAppBarColor() {
      if (
        !!document.documentElement.scrollTop &&
        document.documentElement.scrollTop > 100
      ) {
        this.appbarColor = "blue-grey lighten-3";
      } else if (document.documentElement.scrollTop < 100) {
        this.appbarColor = "transparent";
      }
    }
  },
  mounted() {
    window.addEventListener("scroll", this.changeAppBarColor);
  },
  created() {}
};
</script>

<style>
/* Bounce In */
.hvr-bounce-in {
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.5s;
  transition-duration: 0.5s;
}
.hvr-bounce-in:hover,
.hvr-bounce-in:active {
  -webkit-transform: scale(1.3);
  transform: scale(1.3);
  -webkit-transition-timing-function: cubic-bezier(0.47, 2.02, 0.31, -0.36);
  transition-timing-function: cubic-bezier(0.47, 2.02, 0.31, -0.36);
}
.first {
  background-image: url("../../imgs/toolbar.png");
  height: 270px;
  width: 100%;
  background-size: cover;
  position: fixed;
}
</style>

