<template>
  <div v-if="trades" class="hello">
    <div v-for="trade in trades" :key="trade.id">
      {{ trade }}
    </div>
  </div>
</template>

<script>
import { ref } from '@vue/composition-api'
import { createClient, everything } from 'demo-sdk'

export default {
  name: 'HelloWorld',
  setup() {
    const trades = ref([]);
    const client = createClient({
      subscription: {
        url: 'ws://127.0.0.1:42000/v1/graphql'
      }
    });

    let since = new Date();
    since.setMinutes(since.getMinutes() - 5);

    client.chain.subscription
      .demoTrade({ where: { timestamp: { _gt: since.toISOString() } } })
      .get({ ...everything })
      .subscribe({
        next: res => res.forEach(x => trades.value.push(x))
      });

    return {
      trades
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
