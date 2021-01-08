<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item
        label="报损图书ISBN"
        prop="book_ISBN"
        :rules="[
          { required: true, message: '请输入ISBN ', trigger: 'blur' },
          {
            pattern: /^([0-9]|X)$/,
            message: 'ISBN格式有误',
          },
        ]"
      >
        <el-input v-model="form.book_ISBN" />
      </el-form-item>
      <el-form-item
        label="数量"
        prop="book_num"
        :rules="[{ required: true, message: '请输入数量 ', trigger: 'blur' }]"
      >
        <el-input v-model="form.book_num" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      form: {
        book_ISBN: "",
        book_num: "",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(this.form);
      let _this=this;
      if (this.form.book_ISBN&&this.form.book_num) {
        var formData = new FormData();
        formData.append("book_ISBN", this.form.book_ISBN);
        formData.append("book_num", this.form.book_num);
        Axios({
          method: "post",
          url: "/api/catalog/report_loss",
          data: formData,
          // headers:{'Content-Type':"application/json"}
        }).then(function (res) {
          console.log(res);
          if (res.data.status == 0) {
            _this.$message({
              message: "报损成功",
            });
          } else {
            console.log(res);
            _this.$message({
              message: "出错，报损失败！",
              type: "warning",
            });
          }
        });
      } else {
        this.$message({
          message: "请输入要报损的ISBN与数量！",
          type: "warning",
        });
      }
    },
    onCancel() {
      this.form = "";
      this.$message({
        message: "取消!",
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

