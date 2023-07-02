export type User = {
  id: string;
  name: string;
};

export class UserController {
  constructor(private userService: UserService) {}

  create(user: User): User {
    return this.userService.create(user);
  }

  findById(id: string): User {
    return this.userService.findById(id);
  }
}

export class UserService {
  constructor(private userRepository: UserRepository) {}

  create(user: User) {
    return this.userRepository.create(user);
  }

  findById(id: string): User {
    return this.userRepository.findById(id);
  }
}

export class UserRepository {
  create(user: User) {
    return {
      id: "ID001",
      name: "Tanaka",
    } as User;
  }

  findById(id: string): User {
    return {
      id: "ID001",
      name: "Tanaka",
    } as User;
  }
}

function run() {
  const userRepository = new UserRepository();
  const userService = new UserService(userRepository);
  const userController = new UserController(userService);

  console.log(userController.findById("dummy"));
}

run();
