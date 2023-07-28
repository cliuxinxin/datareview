<template>
  <div class="data-display">
    <div class="form-group">
      <label for="instruction">Instruction:</label>
      <textarea id="instruction" v-model="item.instruction" class="small-input"></textarea>
    </div>
    <div class="form-group">
      <label for="input">Input:</label>
      <textarea id="input" v-model="item.input" class="small-input"></textarea>
    </div>
    <div class="form-group">
      <label for="output">Output:</label>
      <textarea id="output" v-model="item.output" class="large-input"></textarea>
    </div>
    <button @click="submitData">提交</button>
  </div>
</template>

<script>
export default {
  name: 'DataDisplay',
  props: {
    selectedItem: Object,
  },
  data() {
    return {
      item: {...this.selectedItem},
    };
  },
  watch: {
    selectedItem: {
      handler(newValue) {
        this.item = {...newValue};
      },
      deep: true,
    },
  },
  methods: {
    submitData() {
      fetch('http://127.0.0.1:5000/data', {  // 修改为你的后端地址
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.item),
      });
    },
  },
}
</script>


<style scoped>
.data-display {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.form-group {
  margin-bottom: 1em;
}

.small-input {
  width: 100%;  /* 设置一个合适的宽度 */
  height: 5vh;  /* 设置一个合适的高度 */
  font-size: 16px;  /* 设置一个合适的字体大小 */
}

.large-input {
  width: 100%;  /* 设置一个合适的宽度 */
  height: 60vh;  /* 设置一个合适的高度 */
  font-size: 18px;  /* 设置一个合适的字体大小 */
}
</style>