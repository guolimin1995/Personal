<template>
  <v-app>
    <core-toolbar />
    <core-view />
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {
    CoreToolbar: () => import("@/components/core/Toolbar"),
    CoreView: () => import("@/components/core/View")
  },
  data: () => ({}),
  created() {}
};
</script>
<style>
</style>

