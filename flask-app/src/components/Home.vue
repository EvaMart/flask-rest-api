<template>
  <div class="hello">
    <h1>Flask API</h1>
    <div class="container">
      <div class="row">
        <div class="col-6-sm">
          <input v-model="tool_name" placeholder="Enter tool name">
          <button @click="getTool()">Submit</button>
        </div>
      <div class="row">
        <h3>{{ name }}</h3>
      <div> {{ description }} </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Home',
  data(){
    return {
      name: '',
      description : ''
    }
  },
  methods : {
    getTool(){
      axios({
        method: 'post',
        url: 'http://127.25.0.2:5000/api/get_tool',
        params: {
          tool_name: this.tool_name
        },
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      })
        .then(
          (response) => {
            console.log('NO ERROR HERE')
            this.name = response.data.message.name
            this.description = response.data.message.description
            })
        .catch((error) => {
          console.log(error)
          this.description = 'Error'
          })
      }  
    }
  }
</script>

<style scoped>

</style>
