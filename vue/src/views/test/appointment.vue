<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="预约书籍">
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
import axios from "axios";
export default {
  data() {
    return {
      form: {
        Bname: "",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(this.form);
    //   if (this.form.Sname && this.form.Bname) {
    //     var formData = this.form;
    //     borrow(formData).then((res) => {
    //       if (res == "book_no") {
    //         this.$message({
    //           message: "无此书",
    //           type: "warning",
    //         });
    //       } else if (res == "num_no") {
    //         this.$message({
    //           message: "该书已被借走",
    //           type: "warning",
    //         });
    //       } else if (res == "yes") {
    //         this.$message({
    //           message: "借书成功！"
    //         });
    //       }
    //     });
    //   } else {
    //     this.$message({
    //       message: "信息不全！",
    //       type: "warning",
    //     });
    //   }
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

