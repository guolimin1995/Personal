<template>
  <div>
    <v-app-bar
      color="transparent"
      :hide-on-scroll="true"
      flat
      :elevate-on-scroll="true"
      height="120px"
      src="https://picsum.photos/1920/1080?random"
    >
      <template v-slot:img="{ props }">
        <v-img v-bind="props" gradient="to top right, rgba(0,0,0,.0), rgba(0,0,0,.0)"></v-img>
      </template>
      <v-toolbar-items>
        <v-btn text>HOME</v-btn>
        <v-btn text>DISPLAY</v-btn>
        <v-btn text>INFO</v-btn>
        <v-btn text>ME</v-btn>
        <v-btn text>SKILL</v-btn>
      </v-toolbar-items>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data: () => ({})
};
</script>
<style>
</style>

