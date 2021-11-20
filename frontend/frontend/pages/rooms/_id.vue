<template>
  <div class="bg-gray-50">
    <div class="flex flex-col container mx-auto px-5 py-5">
      <RoomsDetail />
      <div class="mt-8" />
      <MessagesList />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.params.id,
    }
  },
}
</script>
