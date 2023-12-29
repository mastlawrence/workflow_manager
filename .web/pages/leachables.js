import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Card, CardBody, CardHeader, Container, Heading, Image, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
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
  <Container>
  <Image src={`/thesis_logo.PNG`}/>
  <VStack justifyContent={`space-between`}>
  <Card size={`lg`} sx={{"font-family": "Tahoma", "width": "800px", "border": "2px solid", "_hover": {"backgroundColor": "PaleGreen", "transition": "0.3s"}}}>
  <CardHeader>
  <Heading sx={{"font-family": "Tahoma", "font-weight": "500"}}>
  {`Process Leachables Data`}
</Heading>
</CardHeader>
  <CardBody>
  <Text>
  {`card 1`}
</Text>
</CardBody>
</Card>
  <Card size={`lg`} sx={{"font-family": "Tahoma", "width": "800px", "border": "2px solid", "_hover": {"backgroundColor": "LightBlue", "transition": "0.3s"}}}>
  <CardHeader>
  <Heading sx={{"font-family": "Tahoma", "font-weight": "500"}}>
  {`This is card 2`}
</Heading>
</CardHeader>
  <CardBody>
  <Text>
  {`card 2`}
</Text>
</CardBody>
</Card>
  <Card size={`lg`} sx={{"font-family": "Tahoma", "width": "800px", "border": "2px solid", "_hover": {"background-color": "LightGrey", "transition": "0.3s"}}}>
  <CardHeader>
  <Heading sx={{"font-family": "Tahoma", "font-weight": "500"}}>
  {`this is card 3`}
</Heading>
</CardHeader>
  <CardBody>
  <Text>
  {`card 3`}
</Text>
</CardBody>
</Card>
</VStack>
</Container>
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
