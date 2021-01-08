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
        <el-table-column label="书名" prop="borrow_book_name"> </el-table-column>
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
        // console.log(res);
        if(res.data.data){
          _this.form = res.data.data;
        }
        // console.log(_this.form);
      });
    },
    cancel(index, row) {
      let _this=this;
      console.log(row.reser_id);
      let data=new FormData();
      
      data.append("reser_id",row.reser_id)
      data.append("user_name",row.reser_user_name)
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
          _this.getData();
          // console.log("预约转续借刷新")
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