<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="借阅人账号名称">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="借阅书籍ISBN">
        <el-input v-model="form.book_ISBN" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { borrow } from "@/api/borrow";
import Axios from "axios";
export default {
  data() {
    return {
      form: {
        name: "",
        book_ISBN: "",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(this.form);
      let _this=this;
      if (this.form.name && this.form.book_ISBN) {
        var data = new FormData();
        data.append("user_name",this.form.name)
        data.append("book_ISBN",this.form.book_ISBN.trim())
        Axios({
          method: "post",
          url: "/api/cir/borrow",
          data: data,
        }).then(function (res) {
            _this.$message({
              message: res.data.msg,
              type: "info",
            });
        });
      } else {
        this.$message({
          message: "信息不全！",
          type: "warning",
        });
      }
    },
    onCancel() {
      this.form = "";
      this.$message({
        message: "cancel!",
        type: "warning",
      });
    },
  },
};
</script>

<style scoped>
.line {
  text-align: center;
}
</style>

