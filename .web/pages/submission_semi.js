import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, ButtonGroup, Card, CardBody, HStack, Image, Input, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, NumberDecrementStepper, NumberIncrementStepper, NumberInput, NumberInputField, NumberInputStepper, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import ReactDropzone from "react-dropzone"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])

  const [files, setFiles] = useState([]);

  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <VStack>
  <Image src={`/thesis_logo.PNG`}/>
  {_e => setFiles((files) => [])}
  <Box as={`form`}>
  <VStack>
  <ReactDropzone multiple={true} onDrop={e => setFiles((files) => e)}>
  {({ getRootProps, getInputProps }) => (
    <Box {...getRootProps()}>
    <Input type={`file`} {...getInputProps()}/>
    <Card sx={{"border": "1px dotted", "padding": "5em"}}>
    <CardBody>
    <Text>
    {`drag and drop file here or click to select files`}
  </Text>
  </CardBody>
  </Card>
  </Box>
  )}
</ReactDropzone>
  <HStack>
  <Text>
  {`Actual AET Concentration (µg/mL):`}
</Text>
  <NumberInput onChange={(_e0) => addEvents([Event("state.set_number", {value:_e0})], (_e0))}>
  <NumberInputField/>
  <NumberInputStepper>
  <NumberIncrementStepper/>
  <NumberDecrementStepper/>
</NumberInputStepper>
</NumberInput>
</HStack>
  <HStack>
  <Text sx={{"width": "300px"}}>
  {`Notebook Reference:`}
</Text>
  <Input type={`text`}/>
</HStack>
  <ButtonGroup variant={`outline`}>
  <Button onClick={(_e) => addEvents([Event("state.handle_upload", {files:files}, "uploadFiles")], (_e))}>
  {`Submit`}
</Button>
  <Button onClick={(_e) => addEvents([Event("state.process_ext", {filename:`.web/public/test_data.csv`,AET_conc:state.number})], (_e))}>
  {`process data`}
</Button>
</ButtonGroup>
  <ButtonGroup variant={`outline`}>
  <Button onClick={(_e) => addEvents([Event("_download", {url:`/finished_lowpH.csv`,filename:`finished_lowpH.csv`})], (_e))}>
  {`Download Low pH`}
</Button>
  <Button onClick={(_e) => addEvents([Event("_download", {url:`/finished_highpH.csv`,filename:`finished_highpH.csv`})], (_e))}>
  {`Download High pH`}
</Button>
  <Button onClick={(_e) => addEvents([Event("_download", {url:`/finished_50IPA.csv`,filename:`finished_50IPA.csv`})], (_e))}>
  {`Download 50% IPA`}
</Button>
  <Button onClick={(_e) => addEvents([Event("_download", {url:`/finished_IPA.csv`,filename:`finished_IPA.csv`})], (_e))}>
  {`Download 100% IPA`}
</Button>
  <Button onClick={(_e) => addEvents([Event("_download", {url:`/finished_hexane.csv`,filename:`finished_hexane.csv`})], (_e))}>
  {`Download 100% Hexane`}
</Button>
</ButtonGroup>
</VStack>
</Box>
</VStack>
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
