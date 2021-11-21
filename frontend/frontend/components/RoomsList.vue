<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-xl text-gray-900 font-semibold mt-3 mb-5">Rooms</h1>
        <div class="rounded-xl bg-white overflow-hidden bg-opacity-50">
          <table class="w-full border rounded shadow-md">
            <thead>
              <tr class="text-left text-gray-900 bg-blue-500 bg-opacity-50">
                <th class="text-gray-50 px-4 py-3">Room</th>
                <th class="text-gray-50 px-4 py-3">Created</th>
              </tr>
            </thead>
            <tbody class="bg-white bg-opacity-50">
              <tr v-for="room in rooms" :key="room" class="text-gray-700">
                <td class="px-4 py-3">
                  <div class="flex items-center text-sm">
                    <div>
                      <NuxtLink
                        class="font-semibold text-black hover:underline"
                        :to="{ name: 'rooms-id', params: { id: room.id } }"
                      >
                        <span>
                          {{ room.name }}
                        </span>
                      </NuxtLink>
                    </div>
                  </div>
                </td>
                <td class="px-4 py-3 text-sm">{{ room.created }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      rooms: [
        {
          id: 1,
          name: 'global_chat',
          created: '2021-11-16',
        },
      ],
    }
  },
}
</script>
