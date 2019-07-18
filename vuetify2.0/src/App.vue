<template>
  <v-app>
    <core-toolbar />
    <core-view />
    <core-floatBtn />
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {
    CoreToolbar: () => import("@/components/core/Toolbar"),
    CoreView: () => import("@/components/core/View"),
    CoreFloatBtn: () => import("@/components/core/FloatBtn")
  },
  data: () => ({}),
  created() {}
};
</script>
<style>
</style>

