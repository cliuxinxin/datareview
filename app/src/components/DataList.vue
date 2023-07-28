<template>
  <div class="data-list">
    <div class="list-section">
      <input type="search" v-model="searchTerm" placeholder="搜索..." class="search-box">
      <div class="scrollable" @scroll="handleScroll">
        <ul>
          <li v-for="(item, index) in filteredItems" :key="index" @click="selectItem(item)" :class="{selected: selectedItem === item}">
            {{ item.instruction }}
          </li>
        </ul>
      </div>
    </div>
    <DataDisplay :selectedItem="selectedItem" />
  </div>
</template>


<script>
import DataDisplay from './DataDisplay.vue'

export default {
  name: 'DataList',
  components: {
    DataDisplay,
  },
  data() {
    return {
      items: [],
      selectedItem: null,
      page: 1,
      searchTerm: '',
    };
  },
  computed: {
    filteredItems() {
      if (this.searchTerm === '') {
        return this.items;
      } else {
        return this.items.filter(item => item.instruction.includes(this.searchTerm));
      }
    },
  },
  methods: {
    fetchData(page) {
      fetch(`http://127.0.0.1:5000/data?page=${page}`)
        .then(response => response.json())
        .then(data => {
          this.items = this.items.concat(data);
          
          // 检查是否需要加载更多的数据
          this.$nextTick(() => {
            const { scrollTop, clientHeight, scrollHeight } = this.$el;
            if (scrollTop + clientHeight >= scrollHeight) {
              this.page += 1;
              this.fetchData(this.page);
            }
          });
        });
    },
    selectItem(item) {
      this.selectedItem = item;
    },
    handleScroll(event) {
      const { scrollTop, clientHeight, scrollHeight } = event.target;
      if (scrollTop + clientHeight >= scrollHeight) {
        this.page += 1;
        this.fetchData(this.page);
      }
    },
  },
  created() {
    this.fetchData(this.page);
  },
}
</script>

<style scoped>
.data-list {
  display: flex;
}

.list-section {
  width: 30%;
  display: flex;
  flex-direction: column;
}

.search-box {
  width: 100%;
}

.scrollable {
  overflow-y: auto;
  height: calc(90vh - 40px);  /* 调整这里的值 */
}

ul {
  width: 100%;
}

li {
  text-align: left;  /* 新增规则 */
}

li.selected {
  background-color: #ddd;
}

DataDisplay {
  width: 70%;
}
</style>