<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="还书人">
        <el-input v-model="form.Sname" />
      </el-form-item>
      <el-form-item label="将还书籍">
        <el-input v-model="form.Bname" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit()">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { breturn } from "@/api/breturn";
import axios from "axios";
export default {
  data() {
    return {
      form: {
        Sname: "",
        Bname: "",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(this.form);
      if (this.form.Sname && this.form.Bname) {
        var formData = this.form;
        breturn(formData).then((res) => {
          if (res == "err_book") {
            this.$message({
              message: "馆藏无此书",
              type: "warning",
            });
          } else if (res == "err_num") {
            this.$message({
              message: "该书未被借走",
              type: "warning",
            });
          } else if (res == "yes") {
            this.$message({
              message: "还书成功！"
            });
          }
        });
      } else {
        this.$message({
          message: "信息不全！",
          type: "warning",
        });
      }
    },
    onCancel() {
    this.form='';
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

