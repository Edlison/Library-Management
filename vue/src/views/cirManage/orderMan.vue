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
        :data="form"
        tooltip-effect="dark"
        stripe
        style="width: 100%"
      >
        <el-table-column type="selection" width="45"></el-table-column>
        <!-- <el-table-column label="序号" type="index" width="65"></el-table-column> -->
        <el-table-column label="ISBN" prop="reser_book_isbn"> </el-table-column>
        
        <el-table-column label="姓名" prop="reser_user_name"> </el-table-column>
        <el-table-column label="书名" prop="reser_book_name"> </el-table-column>
        <el-table-column label="预约开始时间" prop="reser_start_time">
        </el-table-column>
        <el-table-column label="预约结束时间" prop="reser_end_time">
        </el-table-column>
        <el-table-column label="操作">
          <template scope="scope">
            <el-button
              type="primary"
              size="small"
              @click="cancel(scope.$index, scope.row)"
              >转借阅</el-button
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
    // tables() {
    //   const search = this.search;
    //   if (search) {
    //     // filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。
    //     // 注意： filter() 不会对空数组进行检测。
    //     // 注意： filter() 不会改变原始数组。
    //     return this.form.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件;
    //       // some() 方法会依次执行数组的每个元素：
    //       // 如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测;
    //       // 如果没有满足条件的元素，则返回false。
    //       // 注意： some() 不会对空数组进行检测。
    //       // 注意： some() 不会改变原始数组。
    //       return Object.keys(data).some((key) => {
    //         // indexOf() 返回某个指定的字符在某个字符串中首次出现的位置，如果没有找到就返回-1；
    //         // 该方法对大小写敏感！所以之前需要toLowerCase()方法将所有查询到内容变为小写。
    //         return String(data[key]).toLowerCase().indexOf(search) > -1;
    //       });
    //     });
    //   }
    //   return this.form;
    // },
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
        url: "/api/cir/get_resr_all",
      }).then(function (res) {
        console.log(res);
        if(res.data.data){
          _this.form = res.data.data;
        }
        console.log(_this.form);
        // if (res.data.data) {
        //   _this.form = res.data.data;
        // }
        //  else {
        //   _this.form = [
        //   ];
        // }
      });
    },
    cancel(index, row) {
      let _this=this;
      console.log(row.reser_id);
      let data=new FormData();
      data.append("reser_id",row.reser_id)
      Axios({
        method: "post",
        url: "/api/cir/resr2borr",
        data: data
      }).then(function (res) {
        console.log(res);
        if (res.data.status == 0) {
          _this.$message({
            message: res.data.msg,
            type: "success",
          });
          _this.formData();
          console.log("预约转续借刷新")
        } else {
          _this.$message({
            message: res.data.msg,
            type: "error",
          });
        }
      });
    },
  },
};
</script>