.PHONY: clean proto

clean:
	@rm ./src/proto/*.py

proto:
	@touch ./src/proto/__init__.py
	@python -m grpc_tools.protoc \
		-I ./message \
		-I ./message/google \
		-I ./message/user \
		--python_out=./src/proto \
		--grpc_python_out=./src/proto \
		./message/helloworld.proto
	@python -m grpc_tools.protoc \
		-I ./message \
		-I ./message/google \
		-I ./message/user \
		--python_out=./src/proto \
		--grpc_python_out=./src/proto \
		./message/user/user.proto


server:
	python -m src.main
.PHONY: server

client:
	python -m src.client
.PHONY: client