/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useRef } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Input, Text } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import { Event, refs, set_val } from "/utils/state"
import ReactDropzone from "react-dropzone"
import { EventLoopContext, StateContexts, UploadFilesContext } from "/utils/context"
import NextHead from "next/head"



export function Text_59b8b3d2e0a3583bccf75d78d01ae029 () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Text>
  {`uploaded file path: ${state__state.uploaded_file_path}`}
</Text>
  )
}

export function Reactdropzone_353622d57bb49dddd1c0e2860eb6eb66 () {
  const [addEvents, connectError] = useContext(EventLoopContext);
  const [filesById, setFilesById] = useContext(UploadFilesContext);
  const ref_default = useRef(null); refs['ref_default'] = ref_default;

  const on_drop_65dafcf47af23567d698a117f4553801 = useCallback(e => setFilesById(filesById => ({...filesById, default: e})), [addEvents, Event, filesById, setFilesById])

  return (
    <ReactDropzone id={`default`} multiple={true} onDrop={on_drop_65dafcf47af23567d698a117f4553801} ref={ref_default}>
  {({ getRootProps, getInputProps }) => (
    <Box {...getRootProps()}>
    <Input type={`file`} {...getInputProps()}/>
    {`upload excel file`}
  </Box>
  )}
</ReactDropzone>
  )
}

export function Button_153bec1ab6ae6418c98bcc7b8afb3b13 () {
  const [addEvents, connectError] = useContext(EventLoopContext);
  const [filesById, setFilesById] = useContext(UploadFilesContext);

  const on_click_4e2d8f20ed65f854cae117923adec0c7 = useCallback((_e) => addEvents([Event("state.state.handle_upload", {files:filesById.default,upload_id:`default`}, "uploadFiles")], (_e), {}), [addEvents, Event, filesById, setFilesById])

  return (
    <Button onClick={on_click_4e2d8f20ed65f854cae117923adec0c7}>
  {`submit data`}
</Button>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Text>
  {`This is a test page`}
</Text>
  <Reactdropzone_353622d57bb49dddd1c0e2860eb6eb66/>
  <Button_153bec1ab6ae6418c98bcc7b8afb3b13/>
  <Text_59b8b3d2e0a3583bccf75d78d01ae029/>
</Fragment>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
