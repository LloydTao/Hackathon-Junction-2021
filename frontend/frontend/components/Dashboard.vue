<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-3xl text-gray-900 font-semibold mt-5">Dashboard</h1>
        <div class="flex items-baseline space-x-2">
          <h1 class="text-xl text-gray-900 font-semibold mt-5">Statistics</h1>
          <img class="w-5 h-5" src="~/assets/stats3.svg" />
        </div>
        <DashboardCards />
        <div class="flex items-baseline space-x-2 mb-5">
          <h1 class="text-xl text-gray-900 font-semibold mt-5">Home chat</h1>
          <img class="w-5 h-5" src="~/assets/chat.svg" />
        </div>
        <DashboardChat />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      user: {
        id: 1,
        username: 'lloydtao',
        role: 'Player',
        created: '2021-11-16',
        rating: 1000,
        status: 1,
      },
    }
  },
}
</script>
