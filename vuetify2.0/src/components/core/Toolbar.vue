<template>
  <v-app-bar
    app
    elevate-on-scroll
    color="#fcb69f"
    class="animated bounceInDown"
    src="../../imgs/back2_1.png"
    height="80"
  >
    <v-toolbar-title>Zerone</v-toolbar-title>
    <template v-slot:img="{ props }">
      <v-img v-bind="props"></v-img>
    </template>

    <v-spacer></v-spacer>

    <v-toolbar-items>
      <v-btn class="hvr-bounce-in" text color="white">HOME</v-btn>
      <v-btn class="hvr-bounce-in" text color="white">DATEFILE</v-btn>
      <v-btn class="hvr-bounce-in" text color="white">ABOUT</v-btn>
      <v-btn class="hvr-bounce-in" text color="white">CONTECTS</v-btn>
    </v-toolbar-items>
  </v-app-bar>
</template>
<style>
/* Bounce In */
.hvr-bounce-in {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.5s;
  transition-duration: 0.5s;
}
.hvr-bounce-in:hover,
.hvr-bounce-in:focus,
.hvr-bounce-in:active {
  -webkit-transform: scale(1.3);
  transform: scale(1.3);
  -webkit-transition-timing-function: cubic-bezier(0.47, 2.02, 0.31, -0.36);
  transition-timing-function: cubic-bezier(0.47, 2.02, 0.31, -0.36);
}
</style>

