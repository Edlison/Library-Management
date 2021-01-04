<template>
  <div class="form" style="margin: 10px 0 0 10px">
    <div class="searchWord">
      <div style="display: inline-block">搜索：</div>
      <el-input
        v-model="search"
        style="display: inline-block; width: 1000px"
        placeholder="请输入搜索内容"
      >
      </el-input>
    </div>
    <div class="formData">
      <el-table
        ref="formTable"
        :data="tables"
        tooltip-effect="dark"
        stripe
        style="width: 100%"
      >
        <el-table-column type="selection" width="45"></el-table-column>
        <el-table-column label="序号" type="index" width="65"></el-table-column>
        <el-table-column label="ISBN" prop="reser_book_isbn"> </el-table-column>
        <el-table-column label="预约时间" prop="reser_start_time">
        </el-table-column>
        <el-table-column label="结束预约时间" prop="reser_end_time">
        </el-table-column>
        <el-table-column label="操作">
          <template scope="scope">
            <el-button
              type="primary"
              size="small"
              @click="interview(scope.$index, scope.row)"
              >取消预约</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      form: [],
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
        return this.form.filter((data) => {
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
      return this.form;
    },
  },
  created: function () {
    this.getdata();
  },
  methods: {
    getdata() {
      var formData = new FormData();
      let _this = this;
      Axios({
        method: "post",
        url: "/api/cir/get_resr",
      }).then(function (res) {
        console.log(res);
        if (res.data.data) {
          _this.form = res.data.data;
        } else {
          _this.form = [
            {
              reser_id: 1,
              reser_user_name: "admin",
              reser_book_isbn: "978-7-5139-1952-4",
              reser_start_time: "",
              reser_end_time: "",
            },
          ];
        }
      });
    },
    interview(index, row) {
      console.log(row.reser_id);
      return;
      Axios({
        method: "post",
        url: "/api/cir/canc_resr",
        data: {
          reser_id: row.reser_id,
        },
      }).then(function (res) {
        console.log(res);
        if (res.data.status == 1) {
          _this.$message({
            message: "成功取消预约",
            type: "success",
          });
        } else {
          _this.$message({
            message: "失败，请重试",
            type: "success",
          });
        }
      });
    },
  },
};
</script>