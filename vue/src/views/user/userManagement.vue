<template>
  <div>
    <el-card class="box-card" style="width: 1000px; margin: 10px 0 0 50px">
      <div style="text-align:center">
        0-超级管理员 1-读者 2/3-采访/编目管理员 4-流通管理员 5-用户管理员
      </div>
    </el-card>
    <div id="depform">
      <div class="searchWord">
        <div style="display: inline-block">搜索：</div>
        <el-input
          v-model="search"
          style="display: inline-block; width: 800px"
          placeholder="请输入搜索内容"
        >
        </el-input>
        <el-button type="primary" @click="addOpen">新增用户</el-button>
      </div>
      <!-- 表格 -->
      <el-table :data="tables" >
        <el-table-column prop="user_name" label="用户名" width="180">
        </el-table-column>
        <!-- <el-table-column prop="user_password" label="密码" width="180">
      </el-table-column> -->
        <el-table-column prop="user_role" label="用户权限" width="200">
        </el-table-column>
        <el-table-column prop="user_borrowing" label="借书数量" width="200">
        </el-table-column>
        <el-table-column prop="user_reserving" label="预约数量" width="200">
        </el-table-column>
        <el-table-column label="操作">
          <template scope="scope">
            <el-button
              type="primary"
              size="small"
              @click="Edit(scope.$index, scope.row)"
              >编辑</el-button
            >
            <el-button type="danger" size="small" @click="Delete(scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <el-dialog
        title="新增"
        :visible.sync="add"
        :modal-append-to-body="false"
        @close="closeadd"
      >
        <el-form
          ref="addform"
          :model="addForm"
          label-width="80px"
          :rules="addrules"
        >
          <el-form-item
            label="用户名"
            prop="user_name"
            :rules="[
              { required: true, message: '请输入用户名 ', trigger: 'blur' },
            ]"
          >
            <el-input v-model="addForm.user_name" />
          </el-form-item>
          <el-form-item
            label="用户密码"
            prop="user_password"
            :rules="[
              { required: true, message: '请输入用户密码 ', trigger: 'blur' },
            ]"
          >
            <el-input v-model="addForm.user_password" />
          </el-form-item>
          <el-form-item label="用户权限" prop="user_role"
                      :rules="[
              { required: true, message: '请输入用户角色 ', trigger: 'blur' },
            ]">
            <el-input
              v-model="addForm.user_role"
            />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="addSubmit">确定增加</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>

      <el-dialog
        title="编辑"
        :visible.sync="editForm"
        size="tiny"
        :modal-append-to-body="false"
        @close="closeEdit"
      >
        <el-form>
          <el-form-item label="用户名" prop="user_name">
            <el-input v-model="editsForm.user_name" :disabled="true" />
          </el-form-item>
          <el-form-item label="用户密码" prop="user_password">
            <el-input v-model="editsForm.user_password" />
          </el-form-item>
          <el-form-item label="用户权限" prop="user_role">
            <el-input v-model="editsForm.user_role" :disabled="true" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="depSubmit">确定修改</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
    </div>
  </div>
</template>
 
  <script>
import Axios from "axios";
import { Form } from "element-ui";
export default {
  data() {
    return {
      search: "",
      addrules: {
        name: [{ required: true, message: "请输入", trigger: "blur" }],
        year: [{ required: true, message: "请输入", trigger: "blur" }],
        role:[{ required: true, message: "请输入", trigger: "blur" }]
      },
      add: false,
      addForm: {},
      editForm: false,
      editsForm: {},
      editsTest: {},
      tableData: [],
    };
  },
  created: function () {
    this.init();
  },
  computed: {
    // 模糊搜索
    tables() {
      const search = this.search;
      if (search) {
        // filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。
        // 注意： filter() 不会对空数组进行检测。
        // 注意： filter() 不会改变原始数组。
        return this.tableData.filter((data) => {
          // some() 方法用于检测数组中的元素是否满足指定条件;
          // some() 方法会依次执行数组的每个元素：
          // 如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测;
          // 如果没有满足条件的元素，则返回false。
          // 注意： some() 不会对空数组进行检测。
          // 注意： some() 不会改变原始数组。
          return Object.keys(data).some((key) => {
            // indexOf() 返回某个指定的字符在某个字符串中首次出现的位置，如果没有找到就返回-1；
            // 该方法对大小写敏感！所以之前需要toLowerCase()方法将所有查询到内容变为小写。
            return String(data[key]).indexOf(search) > -1;
          });
        });
      }
      return this.tableData;
    },
  },
  methods: {
    //每页条数改变时触发 选择一页显示多少行
    //获取数据
    init() {
      let _this = this;
      Axios({
        method: "post",
        url: "/api/user/get_user_all",
      }).then(function (res) {
        console.log(res);
        if (res.data.status == 0) {
          _this.tableData = res.data.data;
        } else {
          _this.$message({
            message: "获取信息失败",
            type: "error",
          });
        }
      });
    },
    //打开编辑窗口
    Edit(index, row) {
      this.editForm = true;
      this.editsForm = Object.assign({}, row);
      this.editsForm.user_password = "";
      this.editsTest = Object.assign({}, row);
    },
    //上传
    up(data) {
      let _this = this;
      Axios({
        method: "POST",
        url: "/api/upload/anything",
        data: data,
        headers: {
          "Content-Type": "application/json",
        },
      }).then(function (res) {
        if (res.data.code == 200) {
          _this.$message({
            message: "操作成功",
            type: "success",
          });
        } else {
          _this.$message({
            message: "操作失败，请重试",
            type: "error",
          });
        }
        // console.log(res);
      });
    },
    //提交编辑结果
    depSubmit() {
      let _this = this;
      if (this.editsTest.user_password == this.editsForm.user_password) {
        this.$message({
          message: "未进行信息修改",
          type: "warning",
        });
        return;
      }
      var passwordReg = /^[0-9a-zA-Z]*$/;
      if (this.editsForm.user_password.length < 6) {
        this.$message({
          message: "密码长度需大于6位",
          type: "error",
        });
        return;
      }
      if (passwordReg.test(this.editsForm.user_password)) {
        this.$message({
          message: "密码至少包含一个特殊字符",
          type: "error",
        });
        return;
      }
      let data = new FormData();
      data.append("user_id", this.editsForm.user_id);
      data.append("user_new_password", this.editsForm.user_password);
      Axios({
        method: "post",
        url: "/api/user/change_password",
        data: data,
      }).then(function (res) {
        console.log(res);
        _this.$message({
          message: res.data.msg,
          type: "info",
        });
        // _this.dormitory = res.data.data;
      });
      this.editForm = false;
    },
    //关闭编辑窗口时执行
    closeEdit() {
      this.init();
    },
    //打开新增窗口
    addOpen() {
      (this.add = true), (this.addForm = {});
    },
    //提交新增内容
    addSubmit() {
      let _this = this;
      let data = new FormData();
      data.append("user_name", this.addForm.user_name);
      data.append("user_password", this.addForm.user_password);
      data.append("user_role", this.addForm.user_role);
      var nameReg = /^[0-9a-zA-Z|_]*$/;
      var passwordReg = /^[0-9a-zA-Z]*$/;
      if (!this.addForm.user_name || !this.addForm.user_password) {
        this.$message({
          message: "请输入用户名与密码！",
          type: "error",
        });
        return;
      }
      if (!nameReg.test(this.addForm.user_name)) {
        this.$message({
          message: "用户名只能含有数字、大小写字母与下划线",
          type: "error",
        });
        return;
      }
      if (this.addForm.user_name.length < 6) {
        this.$message({
          message: "用户名长度需大于6位",
          type: "error",
        });
        return;
      }
      if (this.addForm.user_password.length < 6) {
        this.$message({
          message: "密码长度需大于6位",
          type: "error",
        });
        return;
      }
      if (passwordReg.test(this.addForm.user_password)) {
        this.$message({
          message: "密码至少包含一个特殊字符",
          type: "error",
        });
        return;
      }
      var roleReg = /^[0-5]+$/;
      if (!roleReg.test(this.addForm.user_role)) {
        this.$message({
          message: "用户权限仅为1-5",
          type: "error",
        });
        return;
      }
      Axios({
        method: "post",
        url: "/api/user/register",
        data: data,
      }).then(function (res) {
        console.log(res);
        _this.$message({
          message: res.data.msg,
          type: "info",
        });
        // _this.dormitory = res.data.data;
      });
      this.add = false;
    },
    //关闭新增时执行
    closeadd() {
      this.init();
    },
    //取消操作
    cancel() {
      this.addForm = {};
      this.add = false;
      this.editForm = false;
    },
    //删除
    Delete(row) {
      let _this = this;
      let data = new FormData();
      data.append("user_id", row.user_id);
      if (row.user_borrowing != 0 || row.user_reserving != 0) {
        this.$message({
          message: "用户存在借书或预约书记录，不可删除!",
          type: "error",
        });
        return;
      }
      this.$confirm("删除不可撤销，确定删除此条记录？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          Axios({
            method: "POST",
            url: "/api/user/delete_user",
            data: data,
          }).then(function (res) {
            _this.$message({
              message: res.data.msg,
              type: "info",
            });
            _this.init();
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style  scoped>
#depform {
  margin-left: 50px;
  margin-top: 20px;
}
</style>