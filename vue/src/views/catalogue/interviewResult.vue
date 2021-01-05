<template>
  <div class="dormitory" style="margin: 10px 0 0 10px">
    <div class="searchWord">
      <div style="display: inline-block">搜索：</div>
      <el-input
        v-model="search"
        style="display: inline-block; width: 1000px"
        placeholder="请输入搜索内容"
      >
      </el-input>
    </div>
    <div class="dormitoryData">
      <el-table
        ref="dormitoryTable"
        :data="tables"
        tooltip-effect="dark"
        stripe
        style="width: 100%"
      >
        <el-table-column type="selection" width="45"></el-table-column>
        <el-table-column label="序号" type="index" width="65"></el-table-column>
        <el-table-column label="ISBN" prop="book_ISBN"> </el-table-column>
        <el-table-column label="书名" prop="book_name"> </el-table-column>
        <el-table-column label="作者" prop="book_author"> </el-table-column>
        <el-table-column label="出版社" prop="book_public_company">
        </el-table-column>
        <el-table-column label="数量" prop="book_num"> </el-table-column>
        <el-table-column label="价格" prop="book_price"> </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      dormitory: [
      ],
      search: "",
    };
  },
  computed: {
    // 模糊搜索
    tables() {
      const search = this.search;
      if (search) {
        // filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。
        // 注意： filter() 不会对空数组进行检测。
        // 注意： filter() 不会改变原始数组。
        return this.dormitory.filter((data) => {
          // some() 方法用于检测数组中的元素是否满足指定条件;
          // some() 方法会依次执行数组的每个元素：
          // 如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测;
          // 如果没有满足条件的元素，则返回false。
          // 注意： some() 不会对空数组进行检测。
          // 注意： some() 不会改变原始数组。
          return Object.keys(data).some((key) => {
            // indexOf() 返回某个指定的字符在某个字符串中首次出现的位置，如果没有找到就返回-1；
            // 该方法对大小写敏感！所以之前需要toLowerCase()方法将所有查询到内容变为小写。
            return String(data[key]).toLowerCase().indexOf(search) > -1;
          });
        });
      }
      return this.dormitory;
    },
  },
  created:function(){
    this.getdata();
},

  methods: {
      getdata() {
      let _this=this;
      Axios({
        method: "get",
        url: "/api/interview/showinterviews",
      }).then(function (res) {
        _this.dormitory=res.data.data
      });
    }
  },
};
</script>