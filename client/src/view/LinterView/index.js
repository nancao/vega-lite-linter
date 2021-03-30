import React, { Component } from 'react'
import './index.css'
import { Button, Tooltip } from 'antd';
import { InfoCircleOutlined } from '@ant-design/icons';
import 'antd/dist/antd.css'

import getLinter from "../../network/getLinter"
import getFixer from "../../network/getFixer"
import Rule from "./rule"
import Action from "./action"
// import ModalView from "./modalview"

export default class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      violatedRules: [],
      optimizeActions: [],
      fixable: false,
      optimizeSpec: {},
      enablePreview: false
    }
  }

  getLint = async (spec) => {
    let response = await getLinter(spec);
    this.setState({
      violatedRules: response.data
    })
  }

  getFix = async (spec) => {
    let response = await getFixer(spec);
    if (response.data.fixable) {
      this.setState({
        fixable: true,
        optimizeActions: response.data.optimize_actions,
        optimizeSpec: response.data.optimize_spec,
        enablePreview: true
      })
    }
  }

  showOptimizeSpec = () => {
    try {
      this.props.onEndEdit(this.state.optimizeSpec);
    } catch (error) {
      console.log("json parse error:" + error);
    }
  }

  showPreview = () => {
    this.props.togglePreview();
    this.props.setLinterSpec(this.state.optimizeSpec)
  }

  acceptSuggestion = () => {
    try {
      this.props.onEndEdit(this.state.optimizeSpec);
      this.props.togglePreview();
    } catch (error) {
      console.log("json parse error:" + error);
    }
  }

  handleOk = () => {
    this.setState({
      isModalVisible: false
    })
    // this.props.setAnswer(this.props.index, this.state.radioValue)
    try {
      this.props.onEndEdit(this.state.optimizeSpec);
    } catch (error) {
      console.log("json parse error:" + error);
    }

  };

  handleCancel = () => {
    this.props.togglePreview();
  };

  render() {
    let spec = this.props.spec;
    let { enablePreview } = this.state;
    return (
      <div>
        <Button danger onClick={() => this.getLint(spec)}>
          Inspect Specs
        </Button>
        <Tooltip placement="rightTop" title={'Toggle Linter'}>
          <InfoCircleOutlined fill='#08c' height='1em' width='1em' style={{ marginLeft: 10 }} />
        </Tooltip>
        <div className="violated-rules">
          <div style={{ marginLeft: 16 }}>
            <p style={{ fontWeight: 800, margin: 0 }}>Violated Rules:</p>
            {this.state.violatedRules.map((d, i) => {
              return <Rule ruleContent={d} index={i + 1} key={i} />
            })}
          </div>
        </div>

        <br></br>
        <Button danger onClick={() => this.getFix(spec)}>
          Suggest Revision
        </Button>
        <Tooltip placement="rightTop" title={'Toggle Fixer'}>
          <InfoCircleOutlined color='#08c' height='1em' width='1em' style={{ marginLeft: 10 }} />
        </Tooltip>
        <div className="violated-rules">
          <div style={{ marginLeft: 16 }}>
            <p style={{ fontWeight: 800, margin: 0 }}>Fix suggestions:</p>
            {this.state.optimizeActions.map((d, i) => {
              return <Action actionContent={d} index={i + 1} key={i} />
            })}
          </div>
          <br></br>
          <Button onClick={this.showPreview} disabled={!enablePreview}>
            Preview
          </Button>
          <Tooltip placement="rightTop" title={'Toggle Preview'}>
            <InfoCircleOutlined color='#08c' height='1em' width='1em' style={{ marginLeft: 10 }} />
          </Tooltip>

          <Button onClick={this.acceptSuggestion} type="primary" style={{ marginLeft: 20 }}>Accept</Button>
          <Button onClick={this.handleCancel} >Reject</Button>
        </div>
      </div>
    )
  }
}
