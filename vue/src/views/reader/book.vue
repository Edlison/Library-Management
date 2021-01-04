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
        <el-table-column label="ISBN" prop="book_ISBN"> </el-table-column>
        <el-table-column label="书名" prop="book_name"> </el-table-column>
        <el-table-column label="作者" prop="book_author"> </el-table-column>
        <el-table-column label="出版社" prop="book_public_company">
        </el-table-column>
        <el-table-column label="操作">
          <template scope="scope">
            <el-button
              type="primary"
              size="small"
              @click="interview(scope.$index, scope.row)"
              >预约</el-button
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
      let j = [
        // {
        //   book_name: "JavaScript高级程序设计",
        //   book_author: "Nicholas",
        //   book_public_company: "人民邮电出版社",
        //   book_ISBN: "978-7-115-27579-0",
        //   book_class: "TP",
        //   book_num: 1,
        //   book_state: 0,
        //   book_return_reason: "破损",
        // },
        // {
        //   book_name: "乌合之众大众心理研究",
        //   book_author: "古斯塔夫",
        //   book_public_company: "民主与建设出版社",
        //   book_ISBN: "978-7-5139-1952-4",
        //   book_class: "C",
        //   book_num: 5,
        //   book_state: 1,
        // },
      ];
      console.log(JSON.stringify(j));
      var formData = new FormData();
      formData.append("user_name", "edlison");
      formData.append("user_password", "123123");
      let _this = this;
      //   Axios({
      //     method: "post",
      //     url: "/api/user/login",
      //     headers:"multipart/form-data"
      //   }).then(function (res) {
      //       console.log(res);
      //   });
      Axios({
        method: "post",
        url: "/api/cir/get_all_books",
      }).then(function (res) {
        // console.log(res);
        _this.form = res.data.data;
      });
    },
    interview(index, row) {
      Axios({
        method: "post",
        url: "/api/cir/reserve",
        data:{
            "book_ISBN":row.book_ISBN
        }
      }).then(function (res) {
        console.log(res);
      });
    },
  },
};
</script>