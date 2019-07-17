<template>
  <div id="index">
    <Home />
  </div>
</template>

<script>
export default {
  name: "Index",

  components: {
    Home: () => import("@/components/index/Home")
  }
};
</script>