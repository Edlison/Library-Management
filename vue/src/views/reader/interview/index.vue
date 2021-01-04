<template>
  <div class="app-container">
    <el-card class="box-card">
      <div>
        {{ text }}
      </div>
    </el-card>
    <el-form ref="form" :model="form" label-width="120px" :rules="rule">
      <el-form-item label="书名" prop="book_name">
        <el-input v-model="form.book_name" />
      </el-form-item>
      <el-form-item label="作者" prop="book_author">
        <el-input v-model="form.book_author" />
      </el-form-item>
      <el-form-item label="出版社" prop="book_public_company">
        <el-input v-model="form.book_public_company" />
      </el-form-item>
      <el-form-item label="ISBN" prop="book_ISBN">
        <el-input v-model="form.book_ISBN" />
        <div style="margin-top: 10px">
          示例：978-7-115-47066-9，必须使用 -（英文字符）进行分隔
        </div>
        <!-- <el-select
          v-model="form.isbn1"
          placeholder="选择第一段"
          style="margin-right: 10px"
        >
          <el-option label="978" value="978" />
          <el-option label="979" value="979" />
        </el-select>
        <span>——</span>
        <div style="display: inline-block; margin: 0 10px">
          <el-input
            placeholder="第二段（1-5位数字）"
            v-model="form.isbn2"
            ref="recond"
          >
          </el-input>
        </div>
        <span>——</span>
        <div style="display: inline-block; margin: 0 10px">
          <el-input placeholder="第三段（2-5位数字）" v-model="form.isbn3" ref="thrid">
          </el-input>
        </div>
        <span>——</span>
        <div style="margin-top: 10px">
          <div style="display: inline-block; margin-right: 10px" ref="fouth">
            <el-input placeholder="第四段（1-6位数字）" v-model="form.isbn4">
            </el-input>
          </div>
          <span>——</span>
          <div style="display: inline-block; margin: 0 10px" ref="fifth">
            <el-input placeholder="第五段（1位数字）" v-model="form.isbn5">
            </el-input>
          </div>
        </div> -->
      </el-form-item>
      <el-form-item label="单价">
        <el-input v-model="form.book_price" />
      </el-form-item>
      <el-form-item label="数量">
        <el-input v-model="form.book_num" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<style scope>
.el-card {
  text-align: center;
  margin: 0 auto 10px auto;
}
.el-select .el-input {
  width: 191px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>
<script>
import { mapGetters } from "vuex";
import Axios from "axios";
export default {
  computed: {
    ...mapGetters(["name"]),
  },
  data() {
    return {
      text: "在此输入您希望图书馆购入的书籍信息",
      form: {
        book_name: "数据库系统概论",
        book_author: "王珊",
        book_public_company: "高等教育出版社",
        book_price: "39.6",
        book_ISBN: "978-7-04-040664-1",
        book_num: "1",
      },
      rule: {
        book_name: [
          { required: true, message: "请输入书名", trigger: "blur" },
          // { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
        book_author: [
          { required: true, message: "请输入作者", trigger: "blur" },
        ],
        book_public_company: [
          { required: true, message: "请输入出版社", trigger: "blur" },
        ],
        book_ISBN: [
          { required: true, message: "请输入ISBN ", trigger: "blur" },
          {
            pattern: /^((978|979)-)?([0-9]{1,5}-[0-9]{1,6}-[0-9]{1,6}-([0-9]|X))$/,
            message: "ISBN格式有误",
          },
        ],
      },
    };
  },

  methods: {
    onSubmit() {
      let _this=this;
      if(!this.form.book_name||!this.form.book_author||!this.form.book_public_company||!this.form.book_ISBN){
        this.$message({
        message: "信息不全!",
        type: "warning",
      });
      return ;
      }
      var formData = new FormData();
      formData.append("book_name", this.form.book_name);
      formData.append("book_author", this.form.book_author);
      formData.append("book_public_company", this.form.book_public_company);
      formData.append("book_price", this.form.book_price);
      formData.append("book_ISBN", this.form.book_ISBN);
      formData.append("book_num", this.form.book_num);
      formData.append("user_id", "1");
      Axios({
        method: "post",
        url: "/api/interview/addinterviews",
        data: formData,
      }).then(function (res) {
        console.log(res)
        if (res.data.status == 0) {
          _this.$message({
            message: "收到您的推荐！",
            type: "success",
          });
        } else {
          _this.$message({
            message: "出错，请重试",
            type: "error",
          });
        }
      });
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



